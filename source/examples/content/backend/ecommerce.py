import pandas as pd
from gurobipy import Model, GRB, quicksum

# Load the data
file_path = '/mnt/data/ecommerce.csv'
data = pd.read_csv(file_path)

# Initialize the model
model = Model("E-commerce Pricing Optimization")

# Create decision variables for the prices
prices = {}
demand = {}
for i, row in data.iterrows():
    product_id = row['Product ID']
    base_price = row['Base Price']
    stock = row['Stock Quantity']
    base_demand = row['Base Demand']
    elasticity = row['Price Elasticity']

    # Price variable
    prices[product_id] = model.addVar(vtype=GRB.CONTINUOUS, name=f"Price_{product_id}", lb=0.8 * base_price)

    # Demand variable based on the elasticity formula
    demand[product_id] = model.addVar(vtype=GRB.CONTINUOUS, name=f"Demand_{product_id}")

# Add the demand elasticity constraints and non-negative demand
for i, row in data.iterrows():
    product_id = row['Product ID']
    base_price = row['Base Price']
    base_demand = row['Base Demand']
    elasticity = row['Price Elasticity']

    model.addConstr(
        demand[product_id] == base_demand * (1 - elasticity * ((prices[product_id] - base_price) / base_price)))
    model.addConstr(demand[product_id] >= 0)  # Non-negative demand constraint

# Add stock constraints
for i, row in data.iterrows():
    product_id = row['Product ID']
    stock = row['Stock Quantity']

    model.addConstr(demand[product_id] <= stock)

# Objective function
revenue = quicksum(prices[prod_id] * demand[prod_id] -
                   (row['Base Shipping Cost'] + (2 * row['Size (kg)'] + 1.5 * row['Weight (kg)']) * demand[prod_id])
                   for prod_id, row in data.set_index('Product ID').iterrows())

model.setObjective(revenue, GRB.MAXIMIZE)

# Optimize the model
model.optimize()

# Collecting results
results = {
    "Product ID": [],
    "Optimal Price": [],
    "Expected Demand": []
}

for prod_id in prices:
    results["Product ID"].append(prod_id)
    results["Optimal Price"].append(prices[prod_id].X)
    results["Expected Demand"].append(demand[prod_id].X)

# Convert the results to a DataFrame for better readability
results_df = pd.DataFrame(results)
