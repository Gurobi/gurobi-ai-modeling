from gurobipy import Model, GRB, quicksum
import matplotlib.pyplot as plt
import numpy as np

# Define data
T = 24
customer_load = [20, 25, 30, 22, 18, 15, 20, 35, 50, 60, 55, 45, 40, 38, 35, 33, 30, 40, 50, 55, 60, 45, 35, 25]
deployments = {
    'D1': {'load': 10, 'duration': 2, 'window': (0, 8)},
    'D2': {'load': 15, 'duration': 1, 'window': (8, 16)},
    'D3': {'load': 20, 'duration': 3, 'window': (15, 22)},
    'D4': {'load': 25, 'duration': 2, 'window': (6, 12)},
    'D5': {'load': 30, 'duration': 1, 'window': (0, 23)},
    'D6': {'load': 10, 'duration': 1, 'window': (0, 8)},
    'D7': {'load': 20, 'duration': 2, 'window': (5, 13)},
    'D8': {'load': 15, 'duration': 3, 'window': (9, 15)},
    'D9': {'load': 25, 'duration': 2, 'window': (14, 21)},
    'D10': {'load': 30, 'duration': 1, 'window': (0, 23)},
}

# Create model
m = Model("deployment_scheduling")

# Add variables
x = m.addVars(deployments.keys(), range(T), vtype=GRB.BINARY, name="x")

# Objective
avg_load = sum(customer_load) / T + sum(d['load'] * d['duration'] for d in deployments.values()) / T
max_deviation = m.addVar(name="max_deviation")

m.addConstrs(
    (max_deviation >= (quicksum(deployments[d]['load'] * x[d, t - k] for d in deployments for k in range(deployments[d]['duration']) if t - k >= 0) + customer_load[t] - avg_load)
     for t in range(T)), name="deviation_pos")
m.addConstrs(
    (max_deviation >= -(quicksum(deployments[d]['load'] * x[d, t - k] for d in deployments for k in range(deployments[d]['duration']) if t - k >= 0) + customer_load[t] - avg_load)
     for t in range(T)), name="deviation_neg")

m.setObjective(max_deviation, GRB.MINIMIZE)

# Constraints
# 1. All deployments must be executed within their specified time window
for d in deployments:
    m.addConstr(quicksum(x[d, t] for t in range(deployments[d]['window'][0], deployments[d]['window'][1] + 1)) == 1, name=f"deployment_{d}")

# 2. The load at any given time should not exceed 100% of the server capacity
m.addConstrs(
    (quicksum(deployments[d]['load'] * x[d, t - k] for d in deployments for k in range(deployments[d]['duration']) if t - k >= 0) + customer_load[t] <= 100
     for t in range(T)), name="capacity")

# Optimize model
m.optimize()

# Extract results
solution = {}
if m.status == GRB.OPTIMAL:
    for d in deployments:
        for t in range(T):
            if x[d, t].X > 0.5:
                solution[d] = t
                break

# Define colors for each deployment
deployment_colors = {
    'D1': 'lightcoral',
    'D2': 'mediumseagreen',
    'D3': 'gold',
    'D4': 'lightskyblue',
    'D5': 'orange',
    'D6': 'orchid',
    'D7': 'palegreen',
    'D8': 'peru',
    'D9': 'cornflowerblue',
    'D10': 'pink'
}

# Initialize deployment load matrix for each deployment
deployment_matrix = np.zeros((len(deployments), T), dtype=float)

# Fill the matrix with the load for each deployment
for idx, (d, start_time) in enumerate(solution.items()):
    load = deployments[d]['load']
    duration = deployments[d]['duration']
    deployment_matrix[idx, start_time:start_time+duration] = load

# Data for plotting
time_slots = np.arange(T)

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(time_slots, customer_load, label='Customer Load', color='skyblue')

# Stack each deployment
for idx, (d, start_time) in enumerate(solution.items()):
    plt.bar(time_slots, deployment_matrix[idx], bottom=customer_load, label=d, color=deployment_colors[d])
    customer_load += deployment_matrix[idx]

plt.axhline(y=100, color='r', linestyle='--', label='Server Capacity')
plt.xlabel('Time Slot')
plt.ylabel('Load')
plt.title('Customer Load and Deployment Load Over Time')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig("schedule.png")
plt.show()
