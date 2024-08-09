import pandas as pd
from gurobipy import Model, GRB
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/mnt/data/testing_strategy.csv')

# Initialize the model
model = Model('TestingOptimization')

# Extract unique values
os_list = data['OS'].unique()
env_list = data['Testing Environment'].unique()
machine_list = data['Machine'].unique()

# Define decision variables
x = model.addVars(os_list, env_list, machine_list, vtype=GRB.BINARY, name='x')

# Define the objective function
score = {}
current_date = datetime.datetime.now()
for row in data.itertuples():
    testing_date = datetime.datetime.strptime(row._4, "%Y-%m-%d")
    days_since_testing = (current_date - testing_date).days
    score[row.OS, row._2, row.Machine] = days_since_testing * row.Modifier

model.setObjective(sum(score[i, j, k] * x[i, j, k]
                       for i in os_list
                       for j in env_list
                       for k in machine_list
                       if (i, j, k) in score), GRB.MAXIMIZE)

# Add constraints
# Each OS must be tested exactly once
for i in os_list:
    model.addConstr(sum(x[i, j, k] for j in env_list for k in machine_list if (i, j, k) in score) == 1)

# Each testing environment can be chosen at most once
for j in env_list:
    model.addConstr(sum(x[i, j, k] for i in os_list for k in machine_list if (i, j, k) in score) <= 1)

# Optimize the model
model.optimize()

# Extract the selected combinations
selected_combinations = {(i, j, k): x[i, j, k].x for i in os_list for j in env_list for k in machine_list if
                         (i, j, k) in score and x[i, j, k].x > 0}

# Create a DataFrame for selected combinations to match with bars
selected_df = pd.DataFrame(selected_combinations.keys(), columns=['OS', 'Testing Environment', 'Machine'])

# Visualize the results
fig, axs = plt.subplots(2, 2, figsize=(20, 12), sharey=True)

os_map = {'Linux64': (0, 0), 'Armlinux64': (0, 1), 'MacOS': (1, 0), 'Windows': (1, 1)}
palette = sns.color_palette("husl", len(env_list))

for os_name in os_list:
    ax = axs[os_map[os_name]]
    os_data = data[data['OS'] == os_name].copy()
    os_data['Selected'] = os_data.apply(
        lambda row: (row.OS, row['Testing Environment'], row.Machine) in selected_combinations, axis=1)
    os_data['Score'] = os_data.apply(lambda row: score[(row.OS, row['Testing Environment'], row.Machine)], axis=1)

    # Plot the scores and highlight the selected combinations
    bars = sns.barplot(x='Machine', y='Score', hue='Testing Environment', data=os_data, dodge=False, ax=ax,
                       palette=palette)

    # Highlight the correct bars by checking the heights
    for bar in bars.patches:
        height = bar.get_height()
        for idx, row in os_data.iterrows():
            if row['Score'] == height and row['Selected']:
                bar.set_edgecolor('black')
                bar.set_linewidth(4)  # Increase the outline width to twice as big
                break

    ax.set_title(f'{os_name} - Scores and Selected Combinations')
    ax.legend(title='Testing Environment')

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit titles and labels better
plt.show()
