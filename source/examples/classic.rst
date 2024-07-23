Classic OR Examples
===================

.. _diet:

Diet
------------

Builds and solves the classic diet problem. A full-fledged Python version of this problem can be found `here <https://docs.gurobi.com/projects/examples/en/current/examples/python/diet.html>`__.

The prompt to generate a working model could look as follows:

.. code-block:: console

   I want to minimize the cost of food while upholding my dietary needs:

   I want to eat between 1800 and 2200 calories per day.
   At least 91 gram of protein.
   At most 65 gram of fat.
   At most 1779 mg of sodium.
   The portions are non-divisible.

   I want to choose between the following foods:

   food,price,calories,protein,fat,sodium
   hamburger,2.49,410,24,26,730
   chicken,2.89,420,32,10,1190
   hot dog,1.50,560,20,32,1800
   fries,1.89,380,4,19,270
   macaroni,2.09,320,12,10,930
   pizza,1.99,320,15,12,820
   salad,2.49,320,31,12,1230
   milk,0.89,100,8,2.5,125
   ice cream,1.59,330,8,10,180


.. _facility:

Facility
----------------

Simple facility location model: given a set of plants and a set of warehouses, with transportation costs between them,
this example finds the least expensive set of plants to open in order to satisfy product demand.
A full-fledged Python version of this problem can be found `here <https://docs.gurobi.com/projects/examples/en/current/examples/python/facility.html>`__.

.. code-block:: console

   A company currently ships its product from 5 plants to 4 warehouses.
   It is considering closing one or more plants to reduce cost.
   What plant(s) should the company close, in order to minimize transportation and fixed costs?

   Transportation Costs (per 1000 products):

      Plant 1 	Plant 2 	Plant 3 	Plant 4 	Plant 5
   Warehouse 1 	$4,000 	$2,000 	$3,000 	$2,500 	$4,500
   Warehouse 2 	$2,500 	$2,600 	$3,400 	$3,000 	$4,000
   Warehouse 3 	$1,200 	$1,800 	$2,600 	$4,100 	$3,000
   Warehouse 4 	$2,200 	$2,600 	$3,100 	$3,700 	$3,200

   The demand for the warehouses 1-4 is 15, 18, 14, 20 products respectively (per thousand)
   The capacity for the plants 1-5 is 20, 22, 17, 19, 18 products respectively (per thousand)
   The fixed costs for the plants 1-5 is 12000, 15000, 17000, 13000, 16000 respectively

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
