import pandas as pd
from gurobipy import Model, GRB
import datetime as dt

# Load the data
df = pd.read_csv('/mnt/data/devops_testing_strategy.csv')

# Create a model
model = Model('Testing_Optimization')

# Extract sets and parameters
os_list = df['OS'].unique()
env_list = df['Testing Environment'].unique()
machines = {os: df[df['OS'] == os]['Machine'].unique() for os in os_list}
scores = {(row['OS'], row['Machine'], row['Testing Environment']):
          (row['Modifier'] * (dt.datetime.now() - pd.to_datetime(row['Testing Date'])).days)
          for _, row in df.iterrows()}

# Decision variables
x = model.addVars(scores.keys(), vtype=GRB.BINARY, name="x")

# Constraints
# Each OS must be assigned to exactly one testing environment
for os in os_list:
    model.addConstr(
        sum(x[os, m, e] for m in machines[os] for e in env_list if (os, m, e) in scores) == 1,
        name=f"assign_{os}"
    )

# Each testing environment can be used by only one OS
for e in env_list:
    model.addConstr(
        sum(x[os, m, e] for os in os_list for m in machines[os] if (os, m, e) in scores) <= 1,
        name=f"use_env_{e}"
    )

# Objective function
model.setObjective(sum(scores[key] * x[key] for key in scores), GRB.MAXIMIZE)

# Solve the model
model.optimize()

# Display results
if model.status == GRB.OPTIMAL:
    solution = model.getAttr('x', x)
    result = pd.DataFrame([(key[0], key[1], key[2], scores[key]) for key in solution if solution[key] > 0],
                          columns=['OS', 'Machine', 'Testing Environment', 'Score'])
    import ace_tools as tools; tools.display_dataframe_to_user(name="Optimization Results", dataframe=result)
else:
    print("No optimal solution found.")
