import json
import gurobipy as gp
from gurobipy import GRB
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Load the data from the provided JSON file
file_path = '/mnt/data/devops_incident_response.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract data from JSON structure
systems = [system['System'] for system in data]
priority = {system['System']: system['Priority'] for system in data}
recovery_time = {system['System']: system['Recovery Time (minutes)'] for system in data}
dependencies = {system['System']: system['Dependencies'] for system in data}

# Creating the Gurobi model
model = gp.Model("Incident_Response_Optimization")

# Creating decision variables
x = model.addVars(systems, vtype=GRB.BINARY, name="x")
t = model.addVars(systems, vtype=GRB.CONTINUOUS, name="t")

# Decay rate
alpha = 0.0398

# Define the number of breakpoints for the piecewise linear approximation
num_breakpoints = 20
max_time = max(recovery_time.values()) * len(systems)

# Generate the breakpoints and corresponding function values
breakpoints = np.linspace(0, max_time, num_breakpoints)
values = np.exp(-alpha * breakpoints)

# Add additional variables for the piecewise linear approximation
z = model.addVars(systems, num_breakpoints, vtype=GRB.CONTINUOUS, name="z")

# Update the objective function with the piecewise linear approximation
model.setObjective(gp.quicksum(priority[s] * gp.quicksum(values[k] * z[s, k] for k in range(num_breakpoints)) for s in systems), GRB.MAXIMIZE)

# Add constraints to ensure proper piecewise linear approximation
for s in systems:
    model.addConstr(t[s] == gp.quicksum(breakpoints[k] * z[s, k] for k in range(num_breakpoints)), name=f"time_approx_{s}")
    model.addConstr(gp.quicksum(z[s, k] for k in range(num_breakpoints)) == x[s], name=f"sum_z_{s}")

# Re-add constraints
# Dependency constraints
for s in systems:
    for d in dependencies[s]:
        model.addConstr(x[s] <= x[d], name=f"dependency_{s}_{d}")

# Recovery time constraints
for s in systems:
    for d in dependencies[s]:
        model.addConstr(t[s] >= t[d] + recovery_time[d] * x[d], name=f"recovery_time_{s}_{d}")

# Non-negativity constraints
for s in systems:
    model.addConstr(t[s] >= 0, name=f"nonnegativity_{s}")

# Optimize the model
model.optimize()

# Store results in a dictionary
results = {}
for s in systems:
    results[s] = {
        "Recovered": x[s].X,
        "Recovery Time": t[s].X
    }

# Create a directed graph
G = nx.DiGraph()

# Add nodes with recovery time as an attribute
for system, result in results.items():
    G.add_node(system, recovery_time=result['Recovery Time'])

# Add edges based on dependencies
for system, deps in dependencies.items():
    for dep in deps:
        G.add_edge(dep, system)

# Arrange nodes based on recovery time
pos = {system: (results[system]['Recovery Time'], index) for index, system in enumerate(systems)}

# Generate a color map based on initial priority value
priority_values = [priority[system] for system in G.nodes]
colors_priority = [plt.cm.RdYlGn(p / max(priority_values)) for p in priority_values]

# Draw the graph with smaller node size and initial priority value as color
plt.figure(figsize=(20, 10))
nx.draw(G, pos, with_labels=True, node_color=colors_priority, node_size=1000, font_size=10, font_weight='bold', edge_color='gray', arrowsize=20, cmap=plt.cm.RdYlGn)

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn, norm=plt.Normalize(vmin=min(priority_values), vmax=max(priority_values)))
sm.set_array([])
plt.colorbar(sm, label='Initial Priority Value', ax=plt.gca())  # Explicitly specify the axis

plt.xlabel('Recovery Time (minutes)')
plt.title('System Recovery DAG with Initial Priority Values')
plt.show()
