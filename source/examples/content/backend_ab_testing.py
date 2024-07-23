import gurobipy as gp
from gurobipy import GRB
import plotly.graph_objects as go

# Data
user_segments = ["New Users", "Regular Users", "Power Users"]
total_users = [1000, 1500, 500]
disruption = [
    [3, 4, 2, 5, 3, 4, 2, 3, 5, 4],
    [2, 1, 3, 2, 1, 2, 3, 1, 2, 3],
    [1, 2, 1, 3, 2, 1, 1, 2, 3, 2]
]

# Initialize model
model = gp.Model("AB_Test_Optimization")

# Decision variables
x = model.addVars(10, vtype=GRB.BINARY, name="x")
y = model.addVars(3, 10, vtype=GRB.CONTINUOUS, name="y")
slack = model.addVars(3, 10, 10, vtype=GRB.CONTINUOUS, name="slack")

# Objective function
model.setObjective(
    gp.quicksum(disruption[i][j] * y[i,j] for i in range(3) for j in range(10)) +
    gp.quicksum(slack[i,j,k] for i in range(3) for j in range(10) for k in range(j+1, 10)),
    GRB.MINIMIZE
)

# Constraints
# 1. Selection constraint
model.addConstr(gp.quicksum(x[j] for j in range(10)) == 3)

# 2. Allocation constraint
for i in range(3):
    model.addConstr(gp.quicksum(y[i,j] for j in range(10)) == total_users[i])

# 3. Minimum users for statistical significance
for i in range(3):
    for j in range(10):
        model.addConstr(y[i,j] >= 100 * x[j])

# 4. Relaxed Balance constraint
for i in range(3):
    for j in range(10):
        for k in range(j+1, 10):
            model.addConstr(y[i,j] - y[i,k] <= 300 + slack[i,j,k])
            model.addConstr(y[i,k] - y[i,j] <= 300 + slack[i,j,k])

# 5. Linking constraints
for i in range(3):
    for j in range(10):
        model.addConstr(y[i,j] <= total_users[i] * x[j])

# Optimize model
model.optimize()

# Extract results
selected_variants = [j+1 for j in range(10) if x[j].x > 0.5]
allocation = [[y[i,j].x for j in range(10)] for i in range(3)]

# Data from the optimization result
user_segments = ["New Users", "Regular Users", "Power Users"]
selected_variants = [3, 5, 8]
allocation = [
    [0, 0, 400, 0, 300, 0, 0, 300, 0, 0],
    [0, 0, 300, 0, 600, 0, 0, 600, 0, 0],
    [0, 0, 300, 0, 100, 0, 0, 100, 0, 0]
]

# Create labels for the Sankey diagram
labels = ["All Users"] + [f"Variant {v}" for v in selected_variants] + user_segments * len(selected_variants)

# Create sources and targets
sources = [0] * len(selected_variants)  # All users to each variant
targets = list(range(1, len(selected_variants) + 1))  # Variants

# Add sources and targets for user segments
for i, variant in enumerate(selected_variants):
    for j in range(len(user_segments)):
        sources.append(i + 1)
        targets.append(len(selected_variants) + len(user_segments) * i + j + 1)

# Create values (counts)
values = [sum(allocation[j][variant-1] for j in range(len(user_segments))) for variant in selected_variants]
for i, variant in enumerate(selected_variants):
    for j in range(len(user_segments)):
        values.append(allocation[j][variant-1])

# Assign colors to ensure user segments have the same color
color_dict = {
    "All Users": "rgba(128, 128, 128, 0.8)",
    "Variant 3": "rgba(31, 119, 180, 0.8)",
    "Variant 5": "rgba(255, 127, 14, 0.8)",
    "Variant 8": "rgba(44, 160, 44, 0.8)",
    "New Users": "rgba(214, 39, 40, 0.8)",
    "Regular Users": "rgba(148, 103, 189, 0.8)",
    "Power Users": "rgba(140, 86, 75, 0.8)"
}

colors = [color_dict["All Users"]] + [color_dict[f"Variant {v}"] for v in selected_variants]
for segment in user_segments:
    colors += [color_dict[segment]] * len(selected_variants)

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    ))])

fig.update_layout(title_text="User Allocation to Variants and User Segments", font_size=10)

# Save the figure as a PNG file
fig.write_image("sankey_diagram.png")
