from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the CSV files
machines_df = pd.read_csv('/mnt/data/assigning_workloads_machines.csv')
workloads_df = pd.read_csv('/mnt/data/assigning_workloads_workloads.csv')

# Initialize the model
model = Model("Workload Scheduling")

# Sets
machines = machines_df['Machines'].tolist()
workloads = workloads_df['Workloads'].tolist()

# Parameters
vCPU_capacity = dict(zip(machines_df['Machines'], machines_df['vCPU Capacity']))
RAM_capacity = dict(zip(machines_df['Machines'], machines_df['RAM Capacity (GB)']))
GPU_capacity = dict(zip(machines_df['Machines'], machines_df['GPU Capacity (GFLOPS)']))

vCPU_req = dict(zip(workloads_df['Workloads'], workloads_df['vCPU Requirement']))
RAM_req = dict(zip(workloads_df['Workloads'], workloads_df['RAM Requirement (GB)']))
GPU_req = dict(zip(workloads_df['Workloads'], workloads_df['GPU Requirement (GFLOPS)']))

# Decision Variables
x = model.addVars(machines, workloads, vtype=GRB.BINARY, name="x")
y = model.addVars(machines, vtype=GRB.BINARY, name="y")

# Objective: Maximize unused resources only if no workloads are assigned
model.setObjective(
    quicksum(y[m] * (vCPU_capacity[m] + RAM_capacity[m] + GPU_capacity[m]) for m in machines),
    GRB.MAXIMIZE
)

# Constraints
# vCPU capacity constraints
model.addConstrs(
    (quicksum(x[m, w] * vCPU_req[w] for w in workloads) <= vCPU_capacity[m] for m in machines),
    name="vCPU_Capacity"
)

# RAM capacity constraints
model.addConstrs(
    (quicksum(x[m, w] * RAM_req[w] for w in workloads) <= RAM_capacity[m] for m in machines),
    name="RAM_Capacity"
)

# GPU capacity constraints
model.addConstrs(
    (quicksum(x[m, w] * GPU_req[w] for w in workloads) <= GPU_capacity[m] for m in machines),
    name="GPU_Capacity"
)

# Each workload must be scheduled exactly once
model.addConstrs(
    (quicksum(x[m, w] for m in machines) == 1 for w in workloads),
    name="Workload_Assignment"
)

# Adding constraint: if any workload is assigned to a machine, y_m must be 0
model.addConstrs(
    (quicksum(x[m, w] for w in workloads) <= (1 - y[m]) * len(workloads) for m in machines),
    name="No_Workload_Assigned"
)

# Optimize the model
model.optimize()

# Collecting the results
assignments = []
unused_resources = {}
if model.status == GRB.OPTIMAL:
    for m in machines:
        for w in workloads:
            if x[m, w].x > 0.5:  # if assigned
                assignments.append((m, w))
        if y[m].x > 0.5:  # if no workloads are assigned
            unused_resources[m] = {
                "vCPU": vCPU_capacity[m],
                "RAM": RAM_capacity[m],
                "GPU": GPU_capacity[m]
            }

# Display results
print("Assignments:", assignments)
print("Unused Resources:", unused_resources)
