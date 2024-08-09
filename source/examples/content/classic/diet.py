from gurobipy import Model, GRB

# Food data
foods = ["hamburger", "chicken", "hot dog", "fries", "macaroni", "pizza", "salad", "milk", "ice cream"]
prices = [2.49, 2.89, 1.50, 1.89, 2.09, 1.99, 2.49, 0.89, 1.59]
calories = [410, 420, 560, 380, 320, 320, 320, 100, 330]
proteins = [24, 32, 20, 4, 12, 15, 31, 8, 8]
fats = [26, 10, 32, 19, 10, 12, 12, 2.5, 10]
sodiums = [730, 1190, 1800, 270, 930, 820, 1230, 125, 180]

# Create a new model
model = Model("diet")

# Create decision variables for the number of servings of each food
x = model.addVars(len(foods), vtype=GRB.INTEGER, name="x")

# Set objective: minimize the total cost
model.setObjective(sum(prices[i] * x[i] for i in range(len(foods))), GRB.MINIMIZE)

# Add constraints
model.addConstr(sum(calories[i] * x[i] for i in range(len(foods))) >= 1800, "cal_min")
model.addConstr(sum(calories[i] * x[i] for i in range(len(foods))) <= 2200, "cal_max")
model.addConstr(sum(proteins[i] * x[i] for i in range(len(foods))) >= 91, "protein_min")
model.addConstr(sum(fats[i] * x[i] for i in range(len(foods))) <= 65, "fat_max")
model.addConstr(sum(sodiums[i] * x[i] for i in range(len(foods))) <= 1779, "sodium_max")

# Optimize the model
model.optimize()

# Display results
results = {}
if model.status == GRB.OPTIMAL:
    results["status"] = "Optimal solution found"
    results["variables"] = {v.varName: v.x for v in model.getVars() if v.x > 0}
    results["total_cost"] = model.objVal
else:
    results["status"] = "No optimal solution found"
