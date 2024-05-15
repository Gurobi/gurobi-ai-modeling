General - Simple
=========================

.. _diet:

Diet
------------

Builds and solves the classic diet problem. Demonstrates model construction and simple model modification – after the initial model is solved, a constraint is added to limit the number of dairy servings.
A Python version of this example can be found `here <https://docs.gurobi.com/projects/examples/en/stable/examples/python/diet.html>`__.

The prompt to generate a working model could look as follows:

.. code-block:: console

   I want to minimize the cost of food while upholding my dietary needs:

   I want to eat between 1800 and 2200 calories per day
   At least 91 gram of protein
   At most 65 gram of fat
   At most 1779 mg of sodium

   The following food I want to choose between is as follows, it is a comma-delimited table with the following columns: food, price, calories, protein, fat, sodium:
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

Simple facility location model: given a set of plants and a set of warehouses, with transportation costs between them, this example finds the least expensive set of plants to open in order to satisfy product demand. This example demonstrates the use of MIP starts — the example computes an initial, heuristic solution and passes that solution to the MIP solver.
A Python version of this example can be found `here <https://docs.gurobi.com/projects/examples/en/stable/examples/python/facility.html>`__.

.. code-block:: console

   A company currently ships its product from 5 plants to 4 warehouses. It is considering closing one or more plants to reduce cost. What plant(s) should the company close, in order to minimize transportation and fixed costs?

   Transportation Costs (per 1000 products)
      Plant 1 	Plant 2 	Plant 3 	Plant 4 	Plant 5
   Warehouse 1 	$4,000 	$2,000 	$3,000 	$2,500 	$4,500
   Warehouse 2 	$2,500 	$2,600 	$3,400 	$3,000 	$4,000
   Warehouse 3 	$1,200 	$1,800 	$2,600 	$4,100 	$3,000
   Warehouse 4 	$2,200 	$2,600 	$3,100 	$3,700 	$3,200

   The demand for the warehouses 1-4 is 15, 18, 14, 20 products respectively (per thousand)
   The capacity for the plants 1-5 is 20, 22, 17, 19, 18 products respectively (per thousand)
   The fixed costs for the plants 1-5 is 12000, 15000, 17000, 13000, 16000 respectively
