import pandas as pd
from gurobipy import Model, GRB

# Load the diet data
diet_data = pd.read_csv('/mnt/data/diet.csv')

# Extract data
foods = diet_data['food'].tolist()
prices = diet_data['price'].tolist()
calories = diet_data['calories'].tolist()
proteins = diet_data['protein'].tolist()
fats = diet_data['fat'].tolist()
sodiums = diet_data['sodium'].tolist()

# Number of food items
n = len(foods)

# Create a model
model = Model("Diet Optimization")

# Decision variables: number of portions of each food item
x = model.addVars(n, vtype=GRB.INTEGER, name="x")

# Objective: Minimize total cost
model.setObjective(sum(prices[i] * x[i] for i in range(n)), GRB.MINIMIZE)

# Constraints:
# 1. Caloric intake between 1800 and 2200 calories
model.addConstr(sum(calories[i] * x[i] for i in range(n)) >= 1800, "MinCalories")
model.addConstr(sum(calories[i] * x[i] for i in range(n)) <= 2200, "MaxCalories")

# 2. Protein intake at least 91 grams
model.addConstr(sum(proteins[i] * x[i] for i in range(n)) >= 91, "MinProtein")

# 3. Fat intake at most 65 grams
model.addConstr(sum(fats[i] * x[i] for i in range(n)) <= 65, "MaxFat")

# 4. Sodium intake at most 1779 mg
model.addConstr(sum(sodiums[i] * x[i] for i in range(n)) <= 1779, "MaxSodium")

# Optimize the model
model.optimize()

# Extract results
solution = {
    "Food": [],
    "Portions": [],
    "Total Cost": model.objVal
}

for i in range(n):
    if x[i].X > 0.001:  # Only show foods that are included in the solution
        solution["Food"].append(foods[i])
        solution["Portions"].append(x[i].X)

solution_df = pd.DataFrame(solution)
solution_df['Total Cost'] = model.objVal
