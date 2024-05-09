Example prompts - intermediate
==============================

.. _portfolio:

Portfolio Optimization
----------------------

An example that solves a financial portfolio optimization model, where the historical return data is stored using the pandas package and the result is plotted using the matplotlib package. It demonstrates the use of pandas, NumPy, and Matplotlib in conjunction with Gurobi.
A Python version of this example can be found `here <https://docs.gurobi.com/projects/examples/en/stable/examples/python/portfolio.html>`_.

To generate the working model we are going to use a data file from the following link: `sample_data.csv <https://github.com/Gurobi/gurobi-ai-modeling/blob/main/docs/source/example_data/portfolio.csv>`_.
This data file should be attached to the prompt. The prompt itself could look as follows:

.. code-block:: console

   I have data on some stocks that I enclosed in dataset.csv

   The columns are the stocks and rows are their value at different time points.

   Step 1: I want to calculate the minimum risk portfolio
   Step 2: Solve for efficient frontier by varying the expected return.
   Step 3: Create a plot with the following
     - Volatility versus expected return for individual stocks (in blue dots) and include an annotation with the stock name
     - Volatility versus expected return for minimum risk portfolio (in green dots)
     - Efficient frontier showing the volatility (green line)
