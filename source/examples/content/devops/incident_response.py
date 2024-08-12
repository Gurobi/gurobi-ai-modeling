import json
import gurobipy as gp
from gurobipy import GRB
import math

# Load data from the JSON file
with open('incident_response.json', 'r') as file:
    data = json.load(file)

# Extract relevant information
systems = [item["System"] for item in data]
priorities = {item["System"]: item["Priority"] for item in data}
dependencies = {item["System"]: item["Dependencies"] for item in data}
recovery_times = {item["System"]: item["Recovery Time (minutes)"] for item in data}

# Set up the model
model = gp.Model("Incident_Response")

# Decision variables
start_times = model.addVars(systems, vtype=GRB.CONTINUOUS, name="start_time")
finish_times = model.addVars(systems, vtype=GRB.CONTINUOUS, name="finish_time")
value_at_finish = model.addVars(systems, vtype=GRB.CONTINUOUS, name="value_at_finish")

# Constraints to ensure dependencies are met
for system in systems:
    for dep in dependencies[system]:
        model.addConstr(start_times[system] >= finish_times[dep])

# Constraints to ensure finish times are correctly calculated
for system in systems:
    model.addConstr(finish_times[system] == start_times[system] + recovery_times[system])

# Defining the piecewise linear approximation for the exponential function
t_values = list(range(0, 121, 10))  # Time intervals (in minutes)
v_values = [math.exp(-0.0398 * t) for t in t_values]  # Corresponding exponential values

for system in systems:
    if priorities[system] > 0:
        model.addGenConstrPWL(finish_times[system], value_at_finish[system], t_values, v_values, "PWL_" + system)
    else:
        model.addConstr(value_at_finish[system] == 0)

# Objective function
model.setObjective(
    gp.quicksum(
        priorities[system] * value_at_finish[system]
        for system in systems
    ),
    GRB.MAXIMIZE
)

# Optimize the model
model.optimize()

# Collect the results
results = {
    "System": [],
    "Start Time (minutes)": [],
    "Finish Time (minutes)": [],
    "Priority": [],
    "Value at Finish Time": []
}

for system in systems:
    start_time = start_times[system].X
    finish_time = finish_times[system].X
    priority = priorities[system]
    value_at_finish_val = value_at_finish[system].X

    results["System"].append(system)
    results["Start Time (minutes)"].append(start_time)
    results["Finish Time (minutes)"].append(finish_time)
    results["Priority"].append(priority)
    results["Value at Finish Time"].append(value_at_finish_val)
