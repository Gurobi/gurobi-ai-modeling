from gurobipy import Model, GRB, quicksum
import pandas as pd

# Load the data
file_path = 'path_to_your_file/ad_selection.csv'
ad_data = pd.read_csv(file_path)

# Parameters
pages = ad_data['Page ID'].unique()
ads = ad_data['Ad ID'].unique()

# Define constants from the problem description
MinCTR = 2.5
LowCTRThreshold = 2.0
HighCTRThreshold = 3.0
MaxAdsPerPage = 3
RelevanceThreshold = 0.7
Budget = 500

# Create a new model
m = Model("Ad_Selection")

# Create variables
x = m.addVars(ads, pages, vtype=GRB.BINARY, name="x")
total_ads_selected = m.addVar(vtype=GRB.CONTINUOUS, name="total_ads_selected")

# Set objective: Maximize revenue
m.setObjective(
    quicksum(x[i, p] * ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'CTR (%)'].values[0] * ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'Revenue per click ($)'].values[0]
            for i in ads for p in pages if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty),
    GRB.MAXIMIZE
)

# Overall CTR Constraint using the total ads selected
total_ctr = quicksum(x[i, p] * ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'CTR (%)'].values[0] for i in ads for p in pages if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty)
m.addConstr(total_ctr >= MinCTR * total_ads_selected, "Overall_CTR")

# Page CTR Constraint
for p in pages:
    low_ctr_ads = quicksum(x[i, p] for i in ads if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty and ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'CTR (%)'].values[0] < LowCTRThreshold)
    high_ctr_ads = quicksum(x[i, p] for i in ads if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty and ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'CTR (%)'].values[0] >= HighCTRThreshold)
    m.addConstr(low_ctr_ads <= high_ctr_ads, f"Page_CTR_{p}")

# Page Ad Constraint
for p in pages:
    for i in ads:
        if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty:
            m.addConstr(x[i, p] <= 1, f"Page_Ad_{i}_{p}")

# User Experience Constraint
for p in pages:
    m.addConstr(
        quicksum(x[i, p] for i in ads if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty) <= MaxAdsPerPage,
        f"MaxAds_{p}"
    )

# Relevance Constraint using total ads selected
total_relevant_ads = quicksum(x[i, p] * (ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'User Interest Match (Yes/No)'].values[0] == 'Yes') for i in ads for p in pages if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty)
m.addConstr(total_relevant_ads >= RelevanceThreshold * total_ads_selected, "Relevance")

# Budget Constraint
m.addConstr(
    quicksum(x[i, p] * ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p), 'Cost per ad ($)'].values[0] for i in ads for p in pages if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty) <= Budget,
    "Budget"
)

# Ensure total_ads_selected equals the number of selected ads
m.addConstr(
    total_ads_selected == quicksum(x[i, p] for i in ads for p in pages if not ad_data.loc[(ad_data['Ad ID'] == i) & (ad_data['Page ID'] == p)].empty),
    "Total_Ads_Selected"
)

# Optimize the model
m.optimize()

# Extract the selected ads
selected_ads = [(i, p) for i in ads for p in pages if x[i, p].X > 0.5]

# Create a DataFrame to show the selected ads
selected_df = pd.DataFrame(selected_ads, columns=['Ad ID', 'Page ID'])
selected_df = pd.merge(selected_df, ad_data, on=['Ad ID', 'Page ID'])

print("Selected Ads:")
print(selected_df)
