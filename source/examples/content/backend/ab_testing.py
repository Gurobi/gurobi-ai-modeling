from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the data from the CSV file
file_path = '/mnt/data/ab_testing.csv'
data = pd.read_csv(file_path)

# Extract relevant data
segments = data['User Segment'].tolist()
variants = [f"V{i}" for i in range(1, 11)]
users = data['Total Users'].tolist()
disruption = data.iloc[:, 2:].values

# Create a new model
model = Model("A/B Testing Variant Selection")

# Decision variables
x = model.addVars(variants, vtype=GRB.BINARY, name="x")
y = model.addVars(segments, variants, vtype=GRB.CONTINUOUS, name="y")

# Objective: Minimize total disruption
model.setObjective(quicksum(disruption[s, v] * y[segments[s], variants[v]]
                            for s in range(len(segments))
                            for v in range(len(variants))), GRB.MINIMIZE)

# Constraint 1: Select exactly 3 variants
model.addConstr(quicksum(x[v] for v in variants) == 3, name="SelectThreeVariants")

# Constraint 2: Minimum users for each chosen variant
for s in range(len(segments)):
    for v in range(len(variants)):
        model.addConstr(y[segments[s], variants[v]] >= 100 * x[variants[v]],
                        name=f"MinUsers_{segments[s]}_{variants[v]}")

# Constraint 3: Allocate all users in each segment
for s in range(len(segments)):
    model.addConstr(quicksum(y[segments[s], variants[v]] for v in range(len(variants))) == users[s],
                    name=f"AllocateAllUsers_{segments[s]}")

# Constraint 4: Balance constraint between any two variants
for s in range(len(segments)):
    for v1 in range(len(variants)):
        for v2 in range(v1 + 1, len(variants)):
            model.addConstr(y[segments[s], variants[v1]] - y[segments[s], variants[v2]] <= 300,
                            name=f"Balance_{segments[s]}_{variants[v1]}_{variants[v2]}")
            model.addConstr(y[segments[s], variants[v2]] - y[segments[s], variants[v1]] <= 300,
                            name=f"Balance_{segments[s]}_{variants[v2]}_{variants[v1]}")

# Optimize the model
model.optimize()

# Extract the results
selected_variants = [v for v in variants if x[v].x > 0.5]
allocation = {segments[s]: {variants[v]: y[segments[s], variants[v]].x for v in range(len(variants))} for s in range(len(segments))}
