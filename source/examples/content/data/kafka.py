from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the data from the uploaded CSV files
brokers_df = pd.read_csv('path_to/kafka_brokers.csv')
topics_df = pd.read_csv('path_to/kafka_topics.csv')
transfer_rates_df = pd.read_csv('path_to/kafka_rates.csv')

# Extract data from dataframes for model input
brokers = brokers_df['Broker_ID'].tolist()
topics = topics_df['Topic_ID'].tolist()

max_partitions_broker = dict(zip(brokers_df['Broker_ID'], brokers_df['Max_Partitions']))
min_partitions_topic = dict(zip(topics_df['Topic_ID'], topics_df['Min_Partitions']))
max_partitions_topic = dict(zip(topics_df['Topic_ID'], topics_df['Max_Partitions']))

transfer_rates = {}
for i, row in transfer_rates_df.iterrows():
    transfer_rates[(row['From_Broker'], row['To_Broker'])] = row['Transfer_Rate']

# Adjust the transfer_rates dictionary to handle self-transfers (which should be zero)
for b in brokers:
    transfer_rates[(b, b)] = 0  # No transfer cost within the same broker

# Create model
model = Model('Kafka_Partition_Optimization')

# Decision variables: x[t,b] = number of partitions of topic t assigned to broker b
x = model.addVars(topics, brokers, vtype=GRB.INTEGER, name="x")

# Objective: Minimize data transfer between brokers
model.setObjective(
    quicksum(transfer_rates[(b1, b2)] * x[t, b1] * x[t, b2] for t in topics for b1 in brokers for b2 in brokers),
    GRB.MINIMIZE
)

# Constraint 1: Partition Capacity Constraint
model.addConstrs(
    (quicksum(x[t, b] for t in topics) <= max_partitions_broker[b] for b in brokers),
    name="PartitionCapacity"
)

# Constraint 2: Topic Partition Constraint
model.addConstrs(
    (quicksum(x[t, b] for b in brokers) >= min_partitions_topic[t] for t in topics),
    name="MinTopicPartitions"
)
model.addConstrs(
    (quicksum(x[t, b] for b in brokers) <= max_partitions_topic[t] for t in topics),
    name="MaxTopicPartitions"
)

# Constraint 3: Broker Load Balance Constraint
total_partitions = quicksum(x[t, b] for t in topics for b in brokers)
average_partitions_per_broker = total_partitions / len(brokers)
model.addConstrs(
    (quicksum(x[t, b] for t in topics) <= 1.2 * average_partitions_per_broker for b in brokers),
    name="LoadBalanceUpper"
)
model.addConstrs(
    (quicksum(x[t, b] for t in topics) >= 0.8 * average_partitions_per_broker for b in brokers),
    name="LoadBalanceLower"
)

# Constraint 4: Partition Distribution Constraint
model.addConstrs(
    (x[t, b] <= 0.4 * quicksum(x[t, b_] for b_ in brokers) for t in topics for b in brokers),
    name="PartitionDistribution"
)

# Optimize model
model.optimize()

# Extract the solution
solution = {t: {b: x[t, b].X for b in brokers} for t in topics}

# Display the solution
for t in topics:
    print(f"Topic {t}:")
    for b in brokers:
        print(f"  Broker {b}: {solution[t][b]} partitions")
