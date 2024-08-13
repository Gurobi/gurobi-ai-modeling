import gurobipy as gp
from gurobipy import GRB

# Sets of shifts and workers
shifts = list(range(1, 15))  # Shift numbers 1 through 14
workers = ["Amy", "Bob", "Cathy", "Dan", "Ed", "Fred", "Gu"]

# Cost per worker
cost = {
    "Amy": 10,
    "Bob": 12,
    "Cathy": 10,
    "Dan": 8,
    "Ed": 8,
    "Fred": 9,
    "Gu": 11
}

# Shift requirements
shift_requirements = {
    1: 3, 2: 2, 3: 4, 4: 2, 5: 5, 6: 4, 7: 3,
    8: 2, 9: 2, 10: 3, 11: 4, 12: 4, 13: 7, 14: 5
}

# Worker availability for each shift
availability = {
    "Amy":   [2, 3, 5, 7, 9, 10, 11, 12, 13, 14],
    "Bob":   [1, 2, 5, 6, 8, 11, 13],
    "Cathy": [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14],
    "Dan":   [2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14],
    "Ed":    [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14],
    "Fred":  [1, 2, 3, 6, 8, 9, 12, 13, 14],
    "Gu":    [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
}

# Create the optimization model
m = gp.Model("shift_scheduling")

# Decision variables: x[w,s] = 1 if worker w is assigned to shift s
x = m.addVars(workers, shifts, vtype=GRB.BINARY, name="x")

# Objective: minimize the total cost
m.setObjective(gp.quicksum(cost[w] * x[w, s] for w in workers for s in shifts), GRB.MINIMIZE)

# Constraints:
# Shift requirement constraints
for s in shifts:
    m.addConstr(gp.quicksum(x[w, s] for w in workers) >= shift_requirements[s], name=f"shift_req_{s}")

# Worker availability constraints
for w in workers:
    for s in shifts:
        if s not in availability[w]:
            m.addConstr(x[w, s] == 0, name=f"availability_{w}_{s}")

# Solve the model
m.optimize()

# Extract results
assignment = {w: [] for w in workers}
for w in workers:
    for s in shifts:
        if x[w, s].X > 0.5:
            assignment[w].append(s)

total_cost = m.objVal
