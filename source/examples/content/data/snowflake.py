from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the CSV file
file_path = '/mnt/data/snowflake.csv'
data = pd.read_csv(file_path)

# Extract data from the dataframe
n = len(data)
compute_costs = data['Compute_Maintenance_Cost'].tolist()
storage_costs = data['Storage_Cost (GB)'].tolist()
performance_improvements = data['Performance_Improvement (%)'].tolist()

# Initialize the model
model = Model("Snowflake_Optimization")

# Decision variables: x_i = 1 if we optimize the query i, otherwise 0
x = model.addVars(n, vtype=GRB.BINARY, name="x")

# Objective: Maximize the average performance improvement
model.setObjective(quicksum(performance_improvements[i] * x[i] for i in range(n)) / n, GRB.MAXIMIZE)

# Constraints

# Compute Maintenance Cost Constraint
model.addConstr(quicksum(compute_costs[i] * x[i] for i in range(n)) <= 20, "Compute_Cost")

# Storage Cost Constraint
model.addConstr(quicksum(storage_costs[i] * x[i] for i in range(n)) <= 45, "Storage_Cost")

# Query Performance Constraint: Ensure at least 20% total performance improvement
total_performance_improvement = sum(performance_improvements)
model.addConstr(quicksum(performance_improvements[i] * x[i] for i in range(n)) >= 0.20 * total_performance_improvement, "Performance_Improvement")

# Optimize the model
model.optimize()

# Extract the results
selected_queries = [i for i in range(n) if x[i].x > 0.5]
total_performance = sum(performance_improvements[i] for i in selected_queries)
average_performance = total_performance / n
total_compute_cost = sum(compute_costs[i] for i in selected_queries)
total_storage_cost = sum(storage_costs[i] for i in selected_queries)
