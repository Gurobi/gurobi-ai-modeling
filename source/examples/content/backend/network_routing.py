from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the data from the CSV files
backend_data_path = '/mnt/data/network_routing_backend.csv'
internal_data_path = '/mnt/data/network_routing_internal.csv'

backend_df = pd.read_csv(backend_data_path)
internal_df = pd.read_csv(internal_data_path)

# Extract relevant data from the dataframes
services = backend_df['Service'].tolist()
gateways = internal_df['Internal Gateway'].unique().tolist()

processing_times = dict(zip(backend_df['Service'], backend_df['Average Processing Time (ms)']))
reliabilities = dict(zip(backend_df['Service'], backend_df['Reliability (percentage)']))
costs = dict(zip(backend_df['Service'], backend_df['Cost per Request ($)']))

internal_routing = {}
for _, row in internal_df.iterrows():
    internal_routing[(row['Backend Service'], row['Internal Gateway'])] = {
        'processing_time': row['Additional Processing Time (ms)'],
        'reliability': row['Additional Reliability (percentage)']
    }

# Create the Gurobi model
model = Model('API_Gateway_Optimization')

# Decision variables
x = model.addVars(services, vtype=GRB.CONTINUOUS, name="x")
y = model.addVars(internal_routing.keys(), vtype=GRB.CONTINUOUS, name="y")

# Objective: Minimize total latency
model.setObjective(
    quicksum(x[i] * processing_times[i] for i in services) +
    quicksum(y[i, j] * internal_routing[i, j]['processing_time'] for i, j in internal_routing.keys()),
    GRB.MINIMIZE
)

# Constraints
# 1. Backend Reliability Constraint
model.addConstr(
    quicksum(x[i] * reliabilities[i] for i in services) >= 99.5,
    name="Backend_Reliability"
)

# 2. Internal Reliability Constraint
model.addConstr(
    quicksum(y[i, j] * internal_routing[i, j]['reliability'] for i, j in internal_routing.keys()) >= 99.5,
    name="Internal_Reliability"
)

# 3. Backend Routing Constraint
model.addConstr(quicksum(x[i] for i in services) == 1, name="Backend_Routing_Total")
for i in services:
    model.addConstr(x[i] <= 0.4, name=f"Backend_Routing_Limit_{i}")

# 4. Internal Routing Constraints
for i in services:
    model.addConstr(quicksum(y[i, j] for j in gateways if (i, j) in y) == 1, name=f"Internal_Routing_Total_{i}")
    for j in gateways:
        if (i, j) in y:
            model.addConstr(y[i, j] <= 0.75, name=f"Internal_Routing_Limit_{i}_{j}")

# 5. Cost Constraint
model.addConstr(
    quicksum(x[i] * costs[i] for i in services) +
    quicksum(y[i, j] * 0.0 for i, j in internal_routing.keys()) <= 0.4,  # Cost on routing is considered zero here for simplicity
    name="Cost_Constraint"
)

# Optimize the model
model.optimize()

# Collect the results
routing_results = {i: x[i].X for i in services}
internal_routing_results = {(i, j): y[i, j].X for i, j in internal_routing.keys()}
