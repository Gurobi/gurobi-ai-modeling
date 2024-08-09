from gurobipy import Model, GRB, quicksum
import pandas as pd
import plotly.express as px

# Read the data
data = pd.read_csv('/home/braam/git/ai-modeling/examples/generated/backend/4.csv')
data.head()

# Create the model
model = Model("E-commerce Pricing")

# Decision variables
P = {}
Q = {}
Revenue = {}

for i in range(len(data)):
    P[i] = model.addVar(lb=0.8 * data.loc[i, 'Base Price'], vtype=GRB.CONTINUOUS, name=f"P_{i}")
    Q[i] = model.addVar(vtype=GRB.CONTINUOUS, name=f"Q_{i}")
    Revenue[i] = P[i] * Q[i] - (data.loc[i, 'Base Shipping Cost'] + 2 * data.loc[i, 'Size (kg)'] + 1.5 * data.loc[i, 'Weight (kg)'])

# Constraints
for i in range(len(data)):
    model.addConstr(Q[i] <= data.loc[i, 'Stock Quantity'], name=f"Stock_{i}")
    model.addConstr(Q[i] == data.loc[i, 'Base Demand'] * (1 - data.loc[i, 'Price Elasticity'] * (P[i] - data.loc[i, 'Base Price']) / data.loc[i, 'Base Price']), name=f"Demand_{i}")
    model.addConstr(P[i] >= 0.8 * data.loc[i, 'Base Price'], name=f"MinPrice_{i}")

# Objective function
model.setObjective(quicksum(Revenue[i] for i in range(len(data))), GRB.MAXIMIZE)

# Optimize the model
model.optimize()

# Extract the results
prices = [P[i].X for i in range(len(data))]
quantities = [Q[i].X for i in range(len(data))]
total_revenue = model.ObjVal

# Display results
results = pd.DataFrame({
    'Product ID': data['Product ID'],
    'Product Name': data['Product Name'],
    'Optimal Price': prices,
    'Quantity Sold': quantities
})

results['Total Revenue'] = results['Optimal Price'] * results['Quantity Sold']
results['Shipping Cost'] = data['Base Shipping Cost'] + 2 * data['Size (kg)'] + 1.5 * data['Weight (kg)']
results['Net Revenue'] = results['Total Revenue'] - results['Shipping Cost']

# Create a 3D scatter plot
fig = px.scatter_3d(results,
                    x='Optimal Price',
                    y='Quantity Sold',
                    z='Net Revenue',
                    color='Product Name',
                    size='Net Revenue',
                    size_max=60,
                    hover_name='Product Name',
                    title='Optimal Price, Quantity Sold, and Net Revenue')

# Adjust the camera settings
camera = dict(
    eye=dict(x=1.5, y=1.5, z=1.5)  # Adjust these values to change the perspective
)

fig.update_layout(scene_camera=camera)

# Save the figure as a PNG file
fig.write_image("3d_scatter_plot.png")
