import pandas as pd
from gurobipy import Model, GRB, quicksum

# Load the data from the provided CSV file
file_path = 'path_to_your_file/ad_selection.csv'
ad_data = pd.read_csv(file_path)

# Clean the data by removing rows with missing values
cleaned_ad_data = ad_data.dropna()

# Extract relevant data from the cleaned DataFrame
pages = cleaned_ad_data['Page ID'].unique()
ads = cleaned_ad_data['Ad ID'].unique()
ctr = cleaned_ad_data.set_index(['Page ID', 'Ad ID'])['CTR (%)'].to_dict()
revenue = cleaned_ad_data.set_index(['Page ID', 'Ad ID'])['Revenue per click ($)'].to_dict()
interest_match = cleaned_ad_data.set_index(['Page ID', 'Ad ID'])['User Interest Match (Yes/No)'].apply(lambda x: 1 if x == 'Yes' else 0).to_dict()
cost = cleaned_ad_data.set_index(['Page ID', 'Ad ID'])['Cost per ad ($)'].to_dict()

# Create a new Gurobi model
model = Model("Ad_Selection")

# Decision variables
x = model.addVars(pages, ads, vtype=GRB.BINARY, name="x")

# Objective: Maximize revenue
model.setObjective(quicksum(revenue[p, a] * ctr[p, a] * x[p, a] for p in pages for a in ads), GRB.MAXIMIZE)

# Constraint 1: Overall CTR Constraint (Reformulated to avoid division by expression)
model.addConstr(
    quicksum(ctr[p, a] * x[p, a] for p in pages for a in ads) >= 2.5 * quicksum(x[p, a] for p in pages for a in ads),
    "Overall_CTR"
)

# Constraint 2: Page CTR Constraint
for p in pages:
    model.addConstrs((x[p, a] == 1) >> (quicksum(x[p, a2] for a2 in ads if ctr[p, a2] > 3.0) >= 1)
                     for a in ads if ctr[p, a] < 2.0)

# Constraint 3: User Experience Constraint (Max 3 ads per page)
model.addConstrs((quicksum(x[p, a] for a in ads) <= 3 for p in pages), "MaxAdsPerPage")

# Constraint 4: Relevance Constraint (At least 70% ads should match user interest)
model.addConstr(
    quicksum(interest_match[p, a] * x[p, a] for p in pages for a in ads) >= 0.7 * quicksum(x[p, a] for p in pages for a in ads),
    "Relevance"
)

# Constraint 5: Budget Constraint
model.addConstr(
    quicksum(cost[p, a] * x[p, a] for p in pages for a in ads) <= 500,
    "Budget"
)

# Optimize the model
model.optimize()

# Extract the results
solution = {(p, a): x[p, a].x for p in pages for a in ads if x[p, a].x > 0.5}

# Calculate total revenue and average CTR
total_revenue = sum(revenue[p, a] * ctr[p, a] for (p, a) in solution.keys())
average_ctr = sum(ctr[p, a] for (p, a) in solution.keys()) / len(solution)

# Output the results
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average CTR: {average_ctr:.2f}%")
print("Selected ads per page:")
for (p, a) in solution.keys():
    print(f"Page {p}, Ad {a}")
