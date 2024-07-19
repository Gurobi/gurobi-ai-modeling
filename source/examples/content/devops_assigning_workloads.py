import gurobipy as gp
from gurobipy import GRB

# Data
machines = {
    "Machine 1": {"vCPU": 32, "RAM": 128, "GPU": 20},
    "Machine 2": {"vCPU": 16, "RAM": 64, "GPU": 15},
    "Machine 3": {"vCPU": 32, "RAM": 64, "GPU": 30},
    "Machine 4": {"vCPU": 8, "RAM": 32, "GPU": 10},
    "Machine 5": {"vCPU": 16, "RAM": 64, "GPU": 15},
    "Machine 6": {"vCPU": 32, "RAM": 128, "GPU": 20},
    "Machine 7": {"vCPU": 8, "RAM": 32, "GPU": 10},
    "Machine 8": {"vCPU": 8, "RAM": 32, "GPU": 10},
}

workloads = {
    "Workload A": {"vCPU": 8, "RAM": 16, "GPU": 5},
    "Workload B": {"vCPU": 16, "RAM": 32, "GPU": 10},
    "Workload C": {"vCPU": 4, "RAM": 8, "GPU": 2},
    "Workload D": {"vCPU": 32, "RAM": 64, "GPU": 25},
    "Workload E": {"vCPU": 2, "RAM": 4, "GPU": 1},
    "Workload F": {"vCPU": 4, "RAM": 16, "GPU": 3},
    "Workload G": {"vCPU": 16, "RAM": 32, "GPU": 12},
    "Workload H": {"vCPU": 8, "RAM": 16, "GPU": 6},
}

# Initialize model
model = gp.Model("workload_allocation")

# Decision variables
x = model.addVars(machines.keys(), workloads.keys(), vtype=GRB.BINARY, name="x")
y = model.addVars(machines.keys(), vtype=GRB.CONTINUOUS, name="y")
z = model.addVars(machines.keys(), vtype=GRB.BINARY, name="z")

# Objective function
model.setObjective(gp.quicksum(y[i] * z[i] for i in machines.keys()), GRB.MINIMIZE)

# Constraints

# Each workload must be assigned to exactly one machine
for j in workloads.keys():
    model.addConstr(gp.quicksum(x[i, j] for i in machines.keys()) == 1, name=f"assign_{j}")

# Resource constraints
for i in machines.keys():
    model.addConstr(gp.quicksum(workloads[j]["vCPU"] * x[i, j] for j in workloads.keys()) <= machines[i]["vCPU"], name=f"vCPU_{i}")
    model.addConstr(gp.quicksum(workloads[j]["RAM"] * x[i, j] for j in workloads.keys()) <= machines[i]["RAM"], name=f"RAM_{i}")
    model.addConstr(gp.quicksum(workloads[j]["GPU"] * x[i, j] for j in workloads.keys()) <= machines[i]["GPU"], name=f"GPU_{i}")

# Calculation of remainder of resources for used machines
for i in machines.keys():
    model.addConstr(y[i] >= (machines[i]["vCPU"] - gp.quicksum(workloads[j]["vCPU"] * x[i, j] for j in workloads.keys())) +
                            (machines[i]["RAM"] - gp.quicksum(workloads[j]["RAM"] * x[i, j] for j in workloads.keys())) +
                            (machines[i]["GPU"] - gp.quicksum(workloads[j]["GPU"] * x[i, j] for j in workloads.keys())), name=f"remainder_{i}")

# Linking z to usage of machines
for i in machines.keys():
    model.addConstr(gp.quicksum(x[i, j] for j in workloads.keys()) >= z[i], name=f"link_z_{i}")
    model.addConstr(gp.quicksum(x[i, j] for j in workloads.keys()) <= len(workloads) * z[i], name=f"upper_link_z_{i}")

# Optimize model
model.optimize()

# Print results
solution = []
for v in model.getVars():
    if v.x > 0:
        solution.append(f"{v.varName}: {v.x}")

import matplotlib.pyplot as plt
import numpy as np

# Calculate total resources for each machine
total_resources = {i: machines[i]["vCPU"] + machines[i]["RAM"] + machines[i]["GPU"] for i in machines.keys()}

# Calculate total requirements for each workload
total_requirements = {j: workloads[j]["vCPU"] + workloads[j]["RAM"] + workloads[j]["GPU"] for j in workloads.keys()}

# Group workloads by assigned machines
assigned_workloads = {i: [] for i in machines.keys()}
for (i, j), var in x.items():
    if var.X > 0:
        assigned_workloads[i].append(total_requirements[j])

# Create bar chart
fig, ax = plt.subplots()

# Bar positions
positions = np.arange(len(machines.keys()))

# Heights for total resources
heights_total = [total_resources[i] for i in machines.keys()]

# Stack workloads
bottoms = np.zeros(len(machines.keys()))
for j in workloads.keys():
    heights = [total_requirements[j] if j in [w for (m, w) in x.keys() if x[m, w].X > 0 and m == i] else 0 for i in machines.keys()]
    ax.bar(positions, heights, bottom=bottoms, label=j)
    bottoms += np.array(heights)

# Total resources bar
ax.bar(positions, heights_total, alpha=0.5, color='gray', label='Total Resources', edgecolor='black')

# Labels and title
ax.set_xticks(positions)
ax.set_xticklabels(machines.keys(), rotation=45, ha="right")
ax.set_ylabel('Sum of Resources (vCPU + RAM + GPU)')
ax.set_title('Machine Resource Utilization with Assigned Workloads')
ax.legend()

# Show plot
plt.tight_layout()
plt.savefig("workloads.png")
plt.show()
