from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the data from the provided CSV files
base_load_data = pd.read_csv('/mnt/data/scheduling_deployments_base_load.csv')
deployments_data = pd.read_csv('/mnt/data/scheduling_deployments_deployments.csv')

# Define parameters
T = len(base_load_data)
customer_load = base_load_data['Customer Load'].tolist()
deployments = {
    f'D{i+1}': {
        'load': deployments_data.loc[i, 'Deployment Load'],
        'duration': deployments_data.loc[i, 'Deployment Duration'],
        'window': (
            deployments_data.loc[i, 'Deployment Start Window Start'],
            deployments_data.loc[i, 'Deployment Start Window End']
        )
    }
    for i in range(len(deployments_data))
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

# Extract the results
if m.status == GRB.OPTIMAL:
    optimal_schedule = pd.DataFrame({
        'Time': range(T),
        'Total Load': [sum(deployments[d]['load'] * x[d, t-k].x for d in deployments for k in range(deployments[d]['duration']) if t - k >= 0) + customer_load[t] for t in range(T)]
    })
    optimal_schedule
else:
    "No optimal solution found."
