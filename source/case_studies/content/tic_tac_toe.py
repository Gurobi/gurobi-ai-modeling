import gurobipy as gp
from gurobipy import GRB

# Create a model
model = gp.Model("3D_TicTacToe")

# Indices for the 3D board
n = 3
indices = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]

# Decision variables
x = model.addVars(indices, vtype=GRB.BINARY, name="X")
o = model.addVars(indices, vtype=GRB.BINARY, name="O")

# Constraints: Each cell can only contain either an X or an O
model.addConstrs((x[i, j, k] + o[i, j, k] == 1 for i, j, k in indices), "CellFill")

# Total number of X's and O's
model.addConstr(gp.quicksum(x[i, j, k] for i, j, k in indices) == 14, "TotalX")
model.addConstr(gp.quicksum(o[i, j, k] for i, j, k in indices) == 13, "TotalO")

# Possible lines on a 3D tic-tac-toe board
lines = []

# Horizontal and vertical lines
for i in range(n):
    for j in range(n):
        lines.append([(i, j, k) for k in range(n)])  # x-direction
        lines.append([(i, k, j) for k in range(n)])  # y-direction
        lines.append([(k, i, j) for k in range(n)])  # z-direction

# Diagonal lines within planes
for i in range(n):
    lines.append([(i, k, k) for k in range(n)])  # Diagonal in yz-plane
    lines.append([(i, k, n-1-k) for k in range(n)])  # Anti-diagonal in yz-plane
    lines.append([(k, i, k) for k in range(n)])  # Diagonal in xz-plane
    lines.append([(k, i, n-1-k) for k in range(n)])  # Anti-diagonal in xz-plane
    lines.append([(k, k, i) for k in range(n)])  # Diagonal in xy-plane
    lines.append([(k, n-1-k, i) for k in range(n)])  # Anti-diagonal in xy-plane

# Diagonal lines across the cube
lines.append([(k, k, k) for k in range(n)])  # Main diagonal
lines.append([(k, k, n-1-k) for k in range(n)])  # Other diagonal
lines.append([(k, n-1-k, k) for k in range(n)])  # Another diagonal
lines.append([(n-1-k, k, k) for k in range(n)])  # Yet another diagonal

# Line completion variables
l_x = model.addVars(len(lines), vtype=GRB.BINARY, name="L_X")
l_o = model.addVars(len(lines), vtype=GRB.BINARY, name="L_O")

# Line completion constraints
for h, line in enumerate(lines):
    model.addConstr(l_x[h] >= gp.quicksum(x[i, j, k] for i, j, k in line) - 2, f"LineCompleteX_{h}")
    model.addConstr(l_o[h] >= gp.quicksum(o[i, j, k] for i, j, k in line) - 2, f"LineCompleteO_{h}")

# Objective: Minimize the total number of completed lines
model.setObjective(gp.quicksum(l_x[h] + l_o[h] for h in range(len(lines))), GRB.MINIMIZE)

# Optimize the model
model.optimize()

# Retrieve the results
objective_value = model.ObjVal
x_solution = model.getAttr('x', x)
o_solution = model.getAttr('x', o)
completed_lines = sum(l_x[h].X + l_o[h].X for h in range(len(lines)))

x_positions = [(i, j, k) for i, j, k in indices if x_solution[i, j, k] > 0.5]
o_positions = [(i, j, k) for i, j, k in indices if o_solution[i, j, k] > 0.5]
