import pandas as pd
import numpy as np
from gurobipy import Model, GRB, quicksum
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '/mnt/data/portfolio.csv'
stock_data = pd.read_csv(file_path)

# Calculate daily returns and covariance matrix
returns = stock_data.drop(columns='Unnamed: 0')
cov_matrix = returns.cov()
mean_returns = returns.mean()

# Number of stocks
num_stocks = len(returns.columns)

# Create Gurobi model
model = Model()

# Suppress Gurobi output
model.setParam("OutputFlag", 0)

# Add variables for the weights of the stocks
weights = model.addVars(num_stocks, lb=0, ub=1, vtype=GRB.CONTINUOUS, name="weights")

# Set the objective to minimize variance (portfolio risk)
portfolio_variance = quicksum(weights[i] * cov_matrix.iloc[i, j] * weights[j]
                              for i in range(num_stocks) for j in range(num_stocks))
model.setObjective(portfolio_variance, GRB.MINIMIZE)

# Add constraint: sum of weights equals 1
model.addConstr(quicksum(weights[i] for i in range(num_stocks)) == 1, "budget")

# Solve for the minimum risk portfolio
model.optimize()

# Extract the weights of the minimum risk portfolio
min_risk_weights = np.array([weights[i].x for i in range(num_stocks)])
min_risk_return = np.dot(min_risk_weights, mean_returns)
min_risk_variance = portfolio_variance.getValue()

# Define a range of target returns
target_returns = np.linspace(mean_returns.min(), mean_returns.max(), 100)

# Arrays to store the results
portfolio_returns = []
portfolio_volatilities = []

# Solve for each target return
for target in target_returns:
    model.reset()
    # Remove the previous target return constraint if it exists
    if model.getConstrByName("target_return"):
        model.remove(model.getConstrByName("target_return"))
    model.addConstr(quicksum(weights[i] * mean_returns[i] for i in range(num_stocks)) == target, "target_return")
    model.optimize()

    # Store results
    portfolio_returns.append(target)
    portfolio_volatilities.append(np.sqrt(portfolio_variance.getValue()))

# Calculate individual stock returns and volatilities
individual_returns = mean_returns.values
individual_volatilities = np.sqrt(np.diag(cov_matrix))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(individual_volatilities, individual_returns, color='blue', label='Individual Stocks')
for i, txt in enumerate(returns.columns):
    plt.annotate(txt, (individual_volatilities[i], individual_returns[i]), fontsize=8)

plt.scatter([np.sqrt(min_risk_variance)], [min_risk_return], color='green', label='Minimum Risk Portfolio')
plt.plot(portfolio_volatilities, portfolio_returns, color='green', linestyle='-', label='Efficient Frontier')

plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier and Individual Stocks')
plt.legend()
plt.grid(True)
plt.show()
