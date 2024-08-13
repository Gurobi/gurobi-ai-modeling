import pandas as pd
from gurobipy import Model, GRB, quicksum

# Load the transportation cost data
file_path = '/mnt/data/facility.csv'
transportation_costs = pd.read_csv(file_path)
# Clean and process the transportation cost data
# Remove dollar signs and commas, then convert to numeric
transportation_costs_cleaned = transportation_costs.applymap(lambda x: float(str(x).replace('$', '').replace(',', '').strip()))

# Rename the columns for easier access
transportation_costs_cleaned.columns = ['Warehouse', 'Plant 1', 'Plant 2', 'Plant 3', 'Plant 4', 'Plant 5']

# Remove any unnecessary indexing rows
transportation_costs_cleaned = transportation_costs_cleaned.set_index('Warehouse')

# Parameters
demand = [15, 18, 14, 20]  # demand for warehouses 1-4 (in thousands)
capacity = [20, 22, 17, 19, 18]  # capacity for plants 1-5 (in thousands)
fixed_costs = [12000, 15000, 17000, 13000, 16000]  # fixed costs for plants 1-5
transportation_costs_matrix = transportation_costs_cleaned.values

# Indices
plants = range(5)
warehouses = range(4)

# Create a new model
m = Model("plant_closing")

# Decision variables
x = m.addVars(plants, warehouses, vtype=GRB.CONTINUOUS, name="x")  # Amount shipped from plant i to warehouse j
y = m.addVars(plants, vtype=GRB.BINARY, name="y")  # Whether plant i is open

# Objective function: minimize total cost
m.setObjective(quicksum(transportation_costs_matrix[i, j] * x[i, j] for i in plants for j in warehouses) +
               quicksum(fixed_costs[i] * y[i] for i in plants), GRB.MINIMIZE)

# Constraints
# 1. Demand constraints: total shipments to each warehouse should meet demand
m.addConstrs((quicksum(x[i, j] for i in plants) == demand[j] for j in warehouses), name="demand")

# 2. Capacity constraints: total shipments from each plant should not exceed its capacity if the plant is open
m.addConstrs((quicksum(x[i, j] for j in warehouses) <= capacity[i] * y[i] for i in plants), name="capacity")

# Optimize model
m.optimize()

# Extract the results
solution_x = m.getAttr('x', x)
solution_y = m.getAttr('x', y)
objective_value = m.ObjVal
