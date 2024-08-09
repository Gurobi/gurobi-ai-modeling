import gurobipy as gp
from gurobipy import GRB

# Data
processing_times = {'A': 200, 'B': 150, 'C': 100, 'D': 120, 'E': 180}
reliabilities = {'A': 99.9, 'B': 99.6, 'C': 99.0, 'D': 99.7, 'E': 99.8}
costs = {'A': 0.30, 'B': 0.25, 'C': 0.10, 'D': 0.15, 'E': 0.20}

additional_times = {
    'A': {'F': 50, 'G': 60, 'H': 55},
    'B': {'H': 40, 'I': 45},
    'C': {'J': 50, 'K': 30, 'L': 35},
    'D': {'M': 25, 'N': 20},
    'E': {'F': 60, 'G': 55}
}

additional_reliabilities = {
    'A': {'F': 99.8, 'G': 99.7, 'H': 99.9},
    'B': {'H': 99.6, 'I': 99.7},
    'C': {'J': 99.8, 'K': 99.5, 'L': 99.6},
    'D': {'M': 99.7, 'N': 99.8},
    'E': {'F': 99.9, 'G': 99.8}
}

additional_costs = {
    'A': {'F': 0.05, 'G': 0.04, 'H': 0.03},
    'B': {'H': 0.02, 'I': 0.03},
    'C': {'J': 0.02, 'K': 0.01, 'L': 0.01},
    'D': {'M': 0.01, 'N': 0.01},
    'E': {'F': 0.04, 'G': 0.03}
}

# Create a new model
m = gp.Model("api_gateway_optimization")

# Variables
x = m.addVars(processing_times.keys(), vtype=GRB.CONTINUOUS, name="x")
y = m.addVars([(i, j) for i in additional_times.keys() for j in additional_times[i].keys()], vtype=GRB.CONTINUOUS, name="y")

# Objective
m.setObjective(
    gp.quicksum(x[i] * processing_times[i] for i in processing_times.keys()) +
    gp.quicksum(y[i, j] * additional_times[i][j] for i in additional_times.keys() for j in additional_times[i].keys()), GRB.MINIMIZE)

# Constraints
# Backend Reliability
m.addConstr(gp.quicksum(x[i] * reliabilities[i] for i in reliabilities.keys()) >= 99.5)

# Internal Reliability
m.addConstr(gp.quicksum(y[i, j] * additional_reliabilities[i][j] for i in additional_reliabilities.keys() for j in additional_reliabilities[i].keys()) >= 99.5)

# Backend Routing
m.addConstr(gp.quicksum(x[i] for i in processing_times.keys()) == 1)
for i in processing_times.keys():
    m.addConstr(x[i] <= 0.40)

# Internal Routing
for i in additional_times.keys():
    m.addConstr(gp.quicksum(y[i, j] for j in additional_times[i].keys()) == 1)
    for j in additional_times[i].keys():
        m.addConstr(y[i, j] <= 0.75)

# Cost constraint
m.addConstr(
    gp.quicksum(x[i] * costs[i] for i in costs.keys()) +
    gp.quicksum(y[i, j] * additional_costs[i][j] for i in additional_costs.keys() for j in additional_costs[i].keys()) <= 0.40)

# Optimize model
m.optimize()

# Display results
if m.status == GRB.OPTIMAL:
    for v in m.getVars():
        print(f'{v.varName}: {v.x}')
    print(f'Optimal objective value: {m.objVal}')
else:
    print('No optimal solution found.')


import matplotlib.pyplot as plt
import networkx as nx

# Create directed graph
G = nx.DiGraph()

# Add nodes for each layer
users = ["Users"]
backends = ["A", "B", "C", "D", "E"]
gateways = ["F", "G", "H", "I", "J", "K", "L", "M", "N"]

# Add edges with flow percentages
flows = {
    ("Users", "A"): 0.0,
    ("Users", "B"): 0.3667,
    ("Users", "C"): 0.2333,
    ("Users", "D"): 0.4,
    ("Users", "E"): 0.0,
    ("A", "F"): 0.75 * 0.0,
    ("A", "G"): 0.0 * 0.0,
    ("A", "H"): 0.25 * 0.0,
    ("B", "H"): 0.75 * 0.3667,
    ("B", "I"): 0.25 * 0.3667,
    ("C", "J"): 0.0 * 0.2333,
    ("C", "K"): 0.75 * 0.2333,
    ("C", "L"): 0.25 * 0.2333,
    ("D", "M"): 0.25 * 0.4,
    ("D", "N"): 0.75 * 0.4,
    ("E", "F"): 0.25 * 0.0,
    ("E", "G"): 0.75 * 0.0,
}

# Define node positions
pos = {
    "Users": (0, 1),
    "A": (1, 2),
    "B": (1, 1.5),
    "C": (1, 1),
    "D": (1, 0.5),
    "E": (1, 0),
    "F": (2, 2.5),
    "G": (2, 2),
    "H": (2, 1.5),
    "I": (2, 1),
    "J": (2, 0.5),
    "K": (2, 0),
    "L": (2, -0.5),
    "M": (2, -1),
    "N": (2, -1.5),
}

# Create the directed graph
for (start, end), flow in flows.items():
    G.add_edge(start, end, weight=flow, label=f"{flow:.2%}")

# Define colors for each layer
colors = {
    "Users": "#1f77b4",  # Blue
    "Backend": "#2ca02c",  # Green
    "Internal": "#d62728"  # Red
}

# Assign colors to nodes
node_colors = []
for node in G.nodes():
    if node == "Users":
        node_colors.append(colors["Users"])
    elif node in backends:
        node_colors.append(colors["Backend"])
    else:
        node_colors.append(colors["Internal"])


# Define a function to draw rectangular nodes with appropriate sizes and colors
def draw_rectangular_nodes(ax, pos, node_colors, size=0.2):
    for node, (x, y) in pos.items():
        ax.add_patch(plt.Rectangle((x - size / 2, y - size / 2), size, size, color=node_colors[node], ec='black'))
        plt.text(x, y, s=node, ha='center', va='center', fontsize=12, color='white')

# Map colors to nodes
node_color_map = {node: colors["Users"] if node == "Users" else (colors["Backend"] if node in backends else colors["Internal"]) for node in G.nodes()}

plt.figure(figsize=(12, 9))
ax = plt.gca()

# Draw rectangular nodes with doubled size
draw_rectangular_nodes(ax, pos, node_color_map, size=0.4)

# Draw edges with doubled width
for (u, v) in G.edges():
    if G[u][v]['weight'] > 0:
        a = nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=G[u][v]['weight'] * 20, arrowstyle='-|>', arrowsize=20)
        a[0].set_joinstyle('miter')
        a[0].set_capstyle("butt")
    else:
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=G[u][v]['weight'] * 20, arrowstyle='-', arrowsize=0)

# Draw edge labels only if the value is non-zero
edge_labels = {(u, v): f"{G[u][v]['weight']:.2%}" for u, v in G.edges() if G[u][v]['weight'] > 0}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Data Flow from Users to Backend Services to Internal Gateways")
plt.axis('off')
plt.savefig('test')