General - Intermediate
==============================

.. _portfolio:

Portfolio Optimization
----------------------

An example that adds some complexity to the :ref:`simple <diet>` examples in which we:

1. utilize data from an external csv file,
2. solve multiple models while varying the expected return (and thus adding risk),
3. plot this data using ``matplotlib``.

Moreover, we do this by giving the LLM only a very limited number of instructions. This is **not** how we would normally
recommend writing your prompt. It so happens to (often) work in this instance.

This example solves a financial portfolio optimization model, using historical return data.
A full-fledged Python version of this problem can be found `here <https://docs.gurobi.com/projects/examples/en/current/examples/python/portfolio.html>`_.

To generate the working model we are going to use a data file from the following link: `portfolio.csv <https://github.com/Gurobi/gurobi-ai-modeling/blob/main/source/examples/example_data/portfolio.csv>`_.
This data file should be attached to the prompt. The prompt itself could look as follows:

.. code-block:: console

   I have data on some stocks that I enclosed in portfolio.csv

   The columns are the stocks and rows are their value at different time points.

   Step 1: I want to calculate the minimum risk portfolio
   Step 2: Solve for efficient frontier by varying the expected return.
   Step 3: Create a plot with the following
     - Volatility versus expected return for individual stocks (in blue dots) and include an annotation with the stock name
     - Volatility versus expected return for minimum risk portfolio (in green dots)
     - Efficient frontier showing the volatility (green line)

   Make sure you set: `model.setParam("OutputFlag", 0)`, to suppress Gurobi output.
