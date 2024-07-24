import gurobipy as gp
from gurobipy import GRB

# Data
transport_cost = [
    [4000, 2000, 3000, 2500, 4500],
    [2500, 2600, 3400, 3000, 4000],
    [1200, 1800, 2600, 4100, 3000],
    [2200, 2600, 3100, 3700, 3200]
]
demand = [15, 18, 14, 20]
capacity = [20, 22, 17, 19, 18]
fixed_cost = [12000, 15000, 17000, 13000, 16000]

# Model
model = gp.Model("Plant_Closure")

# Variables
x = model.addVars(5, 4, vtype=GRB.CONTINUOUS, name="x")
y = model.addVars(5, vtype=GRB.BINARY, name="y")

# Objective
model.setObjective(
    gp.quicksum(transport_cost[j][i] * x[i, j] for i in range(5) for j in range(4)) +
    gp.quicksum(fixed_cost[i] * y[i] for i in range(5)),
    GRB.MINIMIZE
)

# Constraints
# Demand constraints
for j in range(4):
    model.addConstr(gp.quicksum(x[i, j] for i in range(5)) == demand[j], f"demand_{j}")

# Capacity constraints
for i in range(5):
    model.addConstr(gp.quicksum(x[i, j] for j in range(4)) <= capacity[i] * y[i], f"capacity_{i}")

# Optimize
model.optimize()

# Output results
if model.status == GRB.OPTIMAL:
    solution = model.getAttr('x', x)
    plants_open = model.getAttr('x', y)
    total_cost = model.objVal

    results = {
        'total_cost': total_cost,
        'solution': solution,
        'plants_open': plants_open
    }

    optimal_total_cost = f"Optimal total cost: ${total_cost}"
    plant_status = [f"Plant {i+1} open: {int(plants_open[i])}" for i in range(5)]
    shipments = [(f"Ship {solution[i, j]} from Plant {i+1} to Warehouse {j+1}") for i in range(5) for j in range(4) if solution[i, j] > 0]
else:
    results = "No optimal solution found."

import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes for plants and warehouses
plants = ['Plant 1', 'Plant 2', 'Plant 3', 'Plant 4', 'Plant 5']
warehouses = ['Warehouse 1', 'Warehouse 2', 'Warehouse 3', 'Warehouse 4']
G.add_nodes_from(plants, bipartite=0)
G.add_nodes_from(warehouses, bipartite=1)

# Add edges with flow values
flows = {
    (0, 2): 14, (0, 3): 6,
    (1, 0): 14, (1, 3): 8,
    (3, 0): 1, (3, 1): 18,
    (4, 3): 6
}

for (i, j), flow in flows.items():
    if flow > 0:
        G.add_edge(plants[i], warehouses[j], weight=flow, label=f'{flow}')

# Get positions for the nodes
pos = {}
pos.update((node, (1, i)) for i, node in enumerate(plants))
pos.update((node, (2, i)) for i, node in enumerate(warehouses))


# Draw the graph with edge width proportional to shipment amounts, without grid
plt.figure(figsize=(12, 8))

# Compute edge widths based on shipment amounts
edges = G.edges(data=True)
edge_widths = [data['weight'] for _, _, data in edges]
edge_labels = nx.get_edge_attributes(G, 'label')

# Draw nodes
nx.draw_networkx_nodes(G, pos, nodelist=plants, node_color='skyblue', node_size=2000, alpha=0.9)
nx.draw_networkx_nodes(G, pos, nodelist=warehouses, node_color='lightgreen', node_size=2000, alpha=0.9)

# Draw edges with varying widths
edges = nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20, edge_color='gray', width=edge_widths)
for e in edges:
    e.set_joinstyle('miter')
    e.set_capstyle("butt")

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Cross out Plant 3
plt.text(pos['Plant 3'][0], pos['Plant 3'][1], 'Plant 3', horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold', color='red', bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.5'))

# Remove grid
plt.grid(False)

# Show the plot
plt.title('Optimal Plant-Warehouse Shipments and Closed Plant')
plt.savefig("warehouses.png")
