I have difficulty thinking in 3D space
======================================

.. image:: images/tic_tac_toe.png
   :alt: Tic Tac Toe
   :align: center

In one of the modeling examples in our `Jupyter Notebook Modeling Examples <https://www.gurobi.com/jupyter_models/>`__
page, named: `Logic Programming - 3D Tic-Tac-Toe <https://www.gurobi.com/jupyter_models/logic-programming-3d-tic-tac-toe/>`__.

We discuss a problem that aims to minimize the number of lines in a 3-dimensional grid.

Even though, conceptually, the problem is quite easy for a human to understand, however, while playing around with this
example and our Custom GPT, we found inconsistent results. Sometimes yielding the correct answer, but more often, yielding a wrong answer.

Even when the model yielded the correct answer, we often found the generated model to be unsatisfactory, as the model
did not fully correctly model reality. This meant that even though it happened to yield the right answer, changing
the objective would immediately invalidate the model:

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/tic_tac_toe.txt
         :language: text

   .. tab:: Generated Model formulation

      .. include:: content/tic_tac_toe.rst

   .. tab:: Generated Python code

      .. literalinclude:: content/tic_tac_toe.py
         :language: python

In the above example results, both the Model formulation and Python code might initially look good, however
<Somebody knowledgeable should fill this in>