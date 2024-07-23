import gurobipy as gp
from gurobipy import GRB

# Sudoku puzzle
sudoku = [
    [0, 2, 8, 4, 7, 6, 3, 0, 0],
    [0, 0, 0, 8, 3, 9, 0, 2, 0],
    [7, 0, 0, 5, 1, 2, 0, 8, 0],
    [0, 0, 1, 7, 9, 0, 0, 4, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 1, 0, 0],
    [0, 5, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 6, 9, 2, 0, 0, 0, 5],
    [0, 0, 2, 6, 4, 5, 0, 0, 8]
]

# Initialize model
model = gp.Model()

# Decision variables: x[i,j,k] = 1 means cell (i,j) contains number k+1
x = model.addVars(9, 9, 9, vtype=GRB.BINARY, name="x")

# Constraints
# Each cell contains exactly one number
model.addConstrs((gp.quicksum(x[i, j, k] for k in range(9)) == 1 for i in range(9) for j in range(9)), name="Cell")

# Each number appears exactly once in each row
model.addConstrs((gp.quicksum(x[i, j, k] for j in range(9)) == 1 for i in range(9) for k in range(9)), name="Row")

# Each number appears exactly once in each column
model.addConstrs((gp.quicksum(x[i, j, k] for i in range(9)) == 1 for j in range(9) for k in range(9)), name="Column")

# Each number appears exactly once in each 3x3 subgrid
model.addConstrs((
    gp.quicksum(x[i, j, k] for i in range(bi*3, bi*3+3) for j in range(bj*3, bj*3+3)) == 1
    for k in range(9) for bi in range(3) for bj in range(3)), name="Subgrid")

# Pre-filled cells
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            model.addConstr(x[i, j, sudoku[i][j] - 1] == 1)

# Optimize model
model.optimize()

# Extract solution
solution = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        for k in range(9):
            if x[i, j, k].X > 0.5:
                solution[i][j] = k + 1

