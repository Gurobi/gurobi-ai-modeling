import gurobipy as gp
from gurobipy import GRB

# Data
machines = {
    1: {'vCPU': 32, 'RAM': 128, 'GPU': 20000},
    2: {'vCPU': 16, 'RAM': 64, 'GPU': 15000},
    3: {'vCPU': 64, 'RAM': 256, 'GPU': 50000},
    4: {'vCPU': 8, 'RAM': 32, 'GPU': 10000},
    5: {'vCPU': 16, 'RAM': 64, 'GPU': 15000},
    6: {'vCPU': 32, 'RAM': 128, 'GPU': 20000},
    7: {'vCPU': 64, 'RAM': 256, 'GPU': 50000},
    8: {'vCPU': 8, 'RAM': 32, 'GPU': 10000}
}

workloads = {
    'A': {'vCPU': 8, 'RAM': 16, 'GPU': 5000},
    'B': {'vCPU': 16, 'RAM': 32, 'GPU': 10000},
    'C': {'vCPU': 4, 'RAM': 8, 'GPU': 2000},
    'D': {'vCPU': 32, 'RAM': 64, 'GPU': 25000},
    'E': {'vCPU': 2, 'RAM': 4, 'GPU': 1000},
    'F': {'vCPU': 4, 'RAM': 16, 'GPU': 3000},
    'G': {'vCPU': 16, 'RAM': 32, 'GPU': 12000},
    'H': {'vCPU': 8, 'RAM': 16, 'GPU': 6000}
}

# Create model
model = gp.Model("WorkloadScheduling")

# Create decision variables
x = model.addVars(machines.keys(), workloads.keys(), vtype=GRB.BINARY, name="x")
y = model.addVars(machines.keys(), vtype=GRB.BINARY, name="y")

# Objective: Minimize number of machines used
model.setObjective(gp.quicksum(y[m] for m in machines), GRB.MINIMIZE)

# Constraints

# Each workload must be assigned to exactly one machine
for w in workloads:
    model.addConstr(gp.quicksum(x[m, w] for m in machines) == 1, name=f"assign_{w}")

# Capacity constraints
for m in machines:
    model.addConstr(gp.quicksum(workloads[w]['vCPU'] * x[m, w] for w in workloads) <= machines[m]['vCPU'], name=f"vcpu_{m}")
    model.addConstr(gp.quicksum(workloads[w]['RAM'] * x[m, w] for w in workloads) <= machines[m]['RAM'], name=f"ram_{m}")
    model.addConstr(gp.quicksum(workloads[w]['GPU'] * x[m, w] for w in workloads) <= machines[m]['GPU'], name=f"gpu_{m}")

# Link machine usage to workload assignments
for m in machines:
    for w in workloads:
        model.addConstr(x[m, w] <= y[m], name=f"link_{m}_{w}")

# Optimize the model
model.optimize()

# Display results
if model.status == GRB.OPTIMAL:
    used_machines = [m for m in machines if y[m].X > 0.5]
    assignments = {(m, w): x[m, w].X for m in machines for w in workloads if x[m, w].X > 0.5}

    used_machines, assignments, gp.gurobi.version()
else:
    "No optimal solution found."
