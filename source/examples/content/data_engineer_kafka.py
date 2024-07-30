import gurobipy as gp
from gurobipy import GRB

# Define data
brokers = ['B1', 'B2', 'B3', 'B4']
topics = ['T1', 'T2', 'T3', 'T4']
max_partitions = {'B1': 50, 'B2': 60, 'B3': 55, 'B4': 65}
min_partitions = {'T1': 10, 'T2': 15, 'T3': 8, 'T4': 12}
max_partitions_topic = {'T1': 20, 'T2': 25, 'T3': 18, 'T4': 22}

transfer_rates = {
    ('B1', 'B2'): 5, ('B1', 'B3'): 3, ('B1', 'B4'): 4,
    ('B2', 'B1'): 5, ('B2', 'B3'): 4, ('B2', 'B4'): 7,
    ('B3', 'B1'): 3, ('B3', 'B2'): 4, ('B3', 'B4'): 2,
    ('B4', 'B1'): 4, ('B4', 'B2'): 7, ('B4', 'B3'): 2
}

# Create a new model
m = gp.Model('KafkaPartitioning')

# Decision variables
x = m.addVars(topics, brokers, vtype=GRB.INTEGER, name="x")

# Auxiliary variables for products
prod = m.addVars(topics, brokers, brokers, vtype=GRB.CONTINUOUS, name="prod")

# Objective function: Minimize data transfer
m.setObjective(gp.quicksum(transfer_rates[i,j] * prod[t,i,j]
                            for t in topics for i in brokers for j in brokers if i != j), GRB.MINIMIZE)

# Constraints
# Partition capacity constraint
m.addConstrs((gp.quicksum(x[t,b] for t in topics) <= max_partitions[b] for b in brokers), "PartitionCapacity")

# Topic partition constraints
m.addConstrs((gp.quicksum(x[t,b] for b in brokers) >= min_partitions[t] for t in topics), "MinPartitions")
m.addConstrs((gp.quicksum(x[t,b] for b in brokers) <= max_partitions_topic[t] for t in topics), "MaxPartitions")

# Auxiliary variable constraints for products
for t in topics:
    for i in brokers:
        for j in brokers:
            if i != j:
                m.addConstr(prod[t, i, j] == x[t, i] * x[t, j], name=f'prod_{t}_{i}_{j}')

# Broker load balance constraint
avg_partitions = gp.quicksum(x[t,b] for t in topics for b in brokers) / len(brokers)
m.addConstrs((gp.quicksum(x[t,b] for t in topics) <= 1.2 * avg_partitions for b in brokers), "LoadBalanceUpper")
m.addConstrs((gp.quicksum(x[t,b] for t in topics) >= 0.8 * avg_partitions for b in brokers), "LoadBalanceLower")

# Partition distribution constraint
m.addConstrs((x[t,b] <= 0.4 * gp.quicksum(x[t,b_] for b_ in brokers) for t in topics for b in brokers), "PartitionDistribution")

# Optimize the model
m.optimize()

# Display the solution
solution = []
for t in topics:
    for b in brokers:
        if x[t, b].x > 0:
            solution.append((t, b, x[t, b].x))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Extract data for plotting
partition_counts = {b: {t: 0 for t in topics} for b in brokers}

for t, b, count in solution:
    partition_counts[b][t] = count

# Create a stacked bar plot
fig, ax = plt.subplots()

bar_width = 0.5
bar_positions = np.arange(len(brokers))

colors = sns.color_palette("Set2", len(topics))

bottoms = np.zeros(len(brokers))
for i, t in enumerate(topics):
    heights = [partition_counts[b][t] for b in brokers]
    ax.bar(bar_positions, heights, bar_width, bottom=bottoms, label=f'Topic {t}', color=colors[i])
    bottoms += heights

ax.set_xlabel('Brokers')
ax.set_ylabel('Number of Partitions')
ax.set_title('Partition Assignment by Broker and Topic')
ax.set_xticks(bar_positions)
ax.set_xticklabels(brokers)
ax.legend()

plt.savefig("kafka.png")
