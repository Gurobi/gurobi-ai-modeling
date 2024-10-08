import pandas as pd
from gurobipy import Model, GRB

# Load the transportation cost data from the CSV file
file_path = '/mnt/data/facility.csv'
facility_data = pd.read_csv(file_path)

# Data
demands = [15, 18, 14, 20]  # Demand for warehouses 1-4 (in thousands)
capacities = [20, 22, 17, 19, 18]  # Capacity of plants 1-5 (in thousands)
fixed_costs = [12000, 15000, 17000, 13000, 16000]  # Fixed costs for plants 1-5

# Transportation costs (per 1000 products)
transportation_costs = facility_data.iloc[:, 1:].values

# Model
model = Model("Facility Location")

# Decision variables: x[wp] is the amount shipped from plant p to warehouse w
x = model.addVars(len(demands), len(capacities), vtype=GRB.CONTINUOUS, name="x")

# Decision variables: y[p] is 1 if plant p is open, 0 otherwise
y = model.addVars(len(capacities), vtype=GRB.BINARY, name="y")

# Objective: Minimize transportation and fixed costs
model.setObjective(
    sum(transportation_costs[w, p] * x[w, p] for w in range(len(demands)) for p in range(len(capacities))) +
    sum(fixed_costs[p] * y[p] for p in range(len(capacities))),
    GRB.MINIMIZE
)

# Constraints
# 1. Demand satisfaction constraints
for w in range(len(demands)):
    model.addConstr(sum(x[w, p] for p in range(len(capacities))) == demands[w], name=f"Demand_{w}")

# 2. Capacity constraints
for p in range(len(capacities)):
    model.addConstr(sum(x[w, p] for w in range(len(demands))) <= capacities[p] * y[p], name=f"Capacity_{p}")

# Optimize model
model.optimize()

# Extract solution
solution_x = model.getAttr('x', x)
solution_y = model.getAttr('x', y)

# Prepare results for display
result_df = pd.DataFrame({
    'Plant': [f'Plant {p+1}' for p in range(len(capacities))],
    'Open (1/0)': [solution_y[p] for p in range(len(capacities))],
    'Fixed Cost': fixed_costs,
    'Capacity': capacities
})

# Display the result
print(result_df)
