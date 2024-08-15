import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model("investment_planning")

# Parameters
C1_initial = 500000
r = [0.2, 1.5, 1.6, 0.4]  # Return rates for each project

# Decision variables: Amount invested in each project in each year
x = m.addVars(3, 4, vtype=GRB.CONTINUOUS, name="x")

# Intermediate variables: Capital at the start of each year
C = m.addVars(4, vtype=GRB.CONTINUOUS, name="C")

# Objective: Maximize the capital at the start of year 4
m.setObjective(C[3], GRB.MAXIMIZE)

# Constraints

# Initial capital at year 1
m.addConstr(C[0] == C1_initial, "initial_capital")

# Capital at the start of each year
m.addConstr(C[1] == x[0, 0] * (1 + r[0]) + x[0, 1] * (1 + r[1]), "capital_year_2")
m.addConstr(C[2] == x[1, 0] * (1 + r[0]) + x[1, 2] * (1 + r[2]), "capital_year_3")
m.addConstr(C[3] == x[2, 0] * (1 + r[0]) + x[2, 3] * (1 + r[3]), "capital_year_4")

# Full investment constraints
m.addConstr(C[0] == x[0, 0] + x[0, 1], "investment_year_1")
m.addConstr(C[1] == x[1, 0] + x[1, 2], "investment_year_2")
m.addConstr(C[2] == x[2, 0] + x[2, 3], "investment_year_3")

# Investment constraints on specific projects
m.addConstr(x[0, 1] <= 120000, "max_investment_project_2")
m.addConstr(x[1, 2] <= 150000, "max_investment_project_3")
m.addConstr(x[2, 3] <= 100000, "max_investment_project_4")

# Optimize the model
m.optimize()

# Extract results
results = {
    "C1": C[0].X,
    "C2": C[1].X,
    "C3": C[2].X,
    "C4": C[3].X,
    "Investments": {(i+1, j+1): x[i,j].X for i in range(3) for j in range(4)}
}
