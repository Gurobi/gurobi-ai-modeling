import pandas as pd
from gurobipy import Model, GRB, quicksum
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv('/home/braam/git/ai-modeling/examples/generated/backend/3.csv')

# Initialize the model
model = Model("Ad_Placement_Optimization")

# Decision variables
x = {}
for index, row in data.iterrows():
    x[(row['Page ID'], row['Ad ID'])] = model.addVar(vtype=GRB.BINARY, name=f"x_{row['Page ID']}_{row['Ad ID']}")

# Auxiliary variables for total CTR, total ads, and total relevant ads
total_ctr = model.addVar(name="total_ctr")
total_ads = model.addVar(name="total_ads")
total_relevant_ads = model.addVar(name="total_relevant_ads")

# Objective: Maximize revenue
model.setObjective(quicksum(x[(row['Page ID'], row['Ad ID'])] * row['CTR (%)'] * row['Revenue per click ($)'] for index, row in data.iterrows()), GRB.MAXIMIZE)

# Constraints
# Overall CTR Constraint
model.addConstr(total_ctr >= 0.025 * total_ads, "Overall_CTR")

# Total CTR and Total Ads constraints
model.addConstr(total_ctr == quicksum(x[(row['Page ID'], row['Ad ID'])] * row['CTR (%)'] for index, row in data.iterrows()))
model.addConstr(total_ads == quicksum(x[(row['Page ID'], row['Ad ID'])] for index, row in data.iterrows()))

# Page CTR Constraint
for page_id in data['Page ID'].unique():
    low_ctr_ads = [x[(page_id, row['Ad ID'])] for index, row in data.iterrows() if row['Page ID'] == page_id and row['CTR (%)'] < 0.02]
    high_ctr_ads = [x[(page_id, row['Ad ID'])] for index, row in data.iterrows() if row['Page ID'] == page_id and row['CTR (%)'] > 0.03]
    for low_ctr_ad in low_ctr_ads:
        model.addConstr(quicksum(high_ctr_ads) >= low_ctr_ad, f"Page_CTR_{page_id}_{low_ctr_ad}")

# User Experience Constraint
for page_id in data['Page ID'].unique():
    model.addConstr(quicksum(x[(page_id, row['Ad ID'])] for index, row in data.iterrows() if row['Page ID'] == page_id) <= 3, f"User_Experience_{page_id}")

# Relevance Constraint
model.addConstr(total_relevant_ads >= 0.70 * total_ads, "Relevance")

# Total Relevant Ads constraint
model.addConstr(total_relevant_ads == quicksum(x[(row['Page ID'], row['Ad ID'])] for index, row in data.iterrows() if row['User Interest Match (Yes/No)'] == 'Yes'))

# Budget Constraint
model.addConstr(quicksum(x[(row['Page ID'], row['Ad ID'])] * row['Cost per ad ($)'] for index, row in data.iterrows()) <= 500, "Budget")

# Optimize the model
model.optimize()

# Display the results
results = []
for v in model.getVars():
    if v.x > 0 and "x_" in v.varName:
        results.append([v.varName, v.x])
results_df = pd.DataFrame(results, columns=['Variable', 'Value'])

results_df.head()

# Results from the optimization
results = [('x[1,102]', 1.0), ('x[1,114]', 1.0), ('x[1,123]', 1.0), ('x[2,106]', 1.0), ('x[2,127]', 1.0), ('x[2,129]', 1.0),
           ('x[3,117]', 1.0), ('x[3,118]', 1.0), ('x[3,135]', 1.0), ('x[4,112]', 1.0), ('x[4,119]', 1.0), ('x[4,137]', 1.0)]

# Prepare data for the plot
data['Selected'] = data.apply(lambda row: (row['Page ID'], row['Ad ID']) in [(int(var[2]), int(var[4:-1])) for var, val in results], axis=1)
data['Interest Match'] = data['User Interest Match (Yes/No)'].apply(lambda x: 'Interest Match' if x == 'Yes' else 'No Interest Match')
data['Selected'] = data['Selected'].apply(lambda x: 'Selected' if x else 'Not Selected')

# Create the Bubble Chart
fig = px.scatter(
    data,
    x="CTR (%)",
    y="Revenue per click ($)",
    size="Cost per ad ($)",
    color="Selected",
    hover_name="Ad ID",
    facet_col="Page ID",
    symbol="Interest Match",
    title="Ad Selection based on CTR and Revenue per Click (Bubble Size: Cost per ad)",
    labels={
        "CTR (%)": "CTR (%)",
        "Revenue per click ($)": "Revenue per Click ($)",
        "Cost per ad ($)": "Cost per Ad ($)",
        "Selected": "Ad Selection",
        "Interest Match": "Interest Match"
    }
)

# Update the layout for better spacing
fig.update_layout(
    height=500,  # Adjust height as needed
    margin=dict(t=50, b=50),
    legend_title_text='Ad Selection and Interest Match',
)
fig.update_xaxes(tickangle=45, title_standoff=25)  # Adjust the x-axis label spacing

# Show the plot
fig.write_image("ad_selection.png")

