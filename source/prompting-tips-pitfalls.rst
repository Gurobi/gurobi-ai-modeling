Tips and pitfalls
==================

.. _tips:

Tips
-------


Unambiguous problem statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about unambiguous problem statement

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Maximize the coverage of different test environments (EnvA, EnvB, EnvC).
         Prioritize machines that have not been tested on recently (considering the latest test_timestamp).
         Prioritize machines on which the test did not pass last time

   .. tab:: Good

      .. code-block:: text

         Pears are green.


Should variables be considered divisible or not?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In many cases, the LLM will be able to deduce whether the variables involved in the problem should be divisible
or not. For instance, cars are very likely to be non-divisible, while kilograms are likely considered divisible.

However, if this is not unambiguously clear from the item itself, it will be helpful to mention how it
should be considered.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to minimize the cost of food while upholding my dietary needs.

         The following food I want to choose between is as follows, it is a comma-delimited table with the following columns: food, price, calories, protein, fat, sodium:
         salad,2.49,320,31,12,1230

         ...


   .. tab:: Good

      .. code-block:: text

         I want to minimize the cost of food while upholding my dietary needs.
         Portions are non-divisible.

         The following food I want to choose between is as follows, it is a comma-delimited table with the following columns: food, price, calories, protein, fat, sodium:
         salad,2.49,320,31,12,1230

         ...

Avoid unnecessary words or statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you think about how an LLM works, it's all about predicting the next token based on what was given before. The
implication of this is that one should avoid adding unnecessary words lest not to confuse the LLM. Let's take an
example of a bad and good pattern. The following shows a description of the objective of a data flow problem where
data can be sent via any route through the nodes :math:`\{0,1,2,3,4,5\}`:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         ...

         The objective is to find out the maximum amount of data that can be
         transferred from Point 0 (Data Center) to Point 5 (User Hub) per second.


   .. tab:: Good

      .. code-block:: text

         ...

         The objective is to find out the maximum amount of data that can be
         transferred to Point 5 (User Hub) per second.

For a human, the objective should be clear for either version: maximize the flow into Point 5. A machine might have more
difficulty with it and consider multiple options:

- Maximize for Point 5 inflow?
- Maximize for Point 0 outflow?
- Maximize the flow from 0 to 5 and disregard the indirect flows into 5?

Even though the latter examples are clearly wrong and an LLM should be able to account for it, it is exactly these kind
of small nuggets of confusion that compound together to an output that is overall less precise. Unfortunately, the
current generation of LLM's will not tell you the degree of confusion under which they are generating a response.

A very simple solution for this is proposed in the Good example: **keep things simple**.

Supply all necessary (dummy) data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about supply all necessary (dummy) data

.. _pitfalls:

Pitfalls
----------------------

The one thing to always keep in mind is that almost never will the AI model express any doubts about interpreting your question. It will make assumptions and when generating an answer will try to sound authoritative.
This is why you have to make extra sure that you don't fall for any of the pitfalls that lead to bad results, since it might not be obvious where the error lies that tripped up the model.

It is all about removing as many impediments for the AI models as possible so it can focus on the problem at hand.

LLM cannot find wheel or execute code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Depending on the LLM you are using and the number of features it has, intermittent issues might arise.
Generally speaking, the more integrated features, the higher the chance that one of these integrations intermittently fails.

If you see an error message like:

- *It seems that I am currently unable to execute the code directly*
- *I cannot find the .whl feel you are trying to install*

It is likely that your LLM provider is experiencing network issues. In such cases, trying at a later moment often solves
the problem.

Messy problem statement
^^^^^^^^^^^^^^^^^^^^^^^

Typos
"""""
If you confuse a ``0`` with a ``O``, the model might or might not be able to understand what you mean

Mixing data types
"""""""""""""""""
Having both integers and floats in your data definition is......

Too long problem statement
^^^^^^^^^^^^^^^^^^^^^^^^^^
Might be fixed with longer context windows

Too many constraints
""""""""""""""""""""
Too many constraints

Too much inline data
""""""""""""""""""""
Too much inline data

Too many different data collections
"""""""""""""""""""""""""""""""""""
Too many different data collections

Too much preprocessing on the data
""""""""""""""""""""""""""""""""""
Too much preprocessing on the data

Advanced Gurobipy API's
^^^^^^^^^^^^^^^^^^^^^^^
More training is done on the earlier ``gurobipy`` API's. This is not a problem since the ``gurobipy`` API is quite stable.
However, it does mean that the AI model is less prone to using the newest advanced API's which allow for building models with more complex constraints.
For simple models however, these advanced API's should not be needed.

Supply/demand assumptions
^^^^^^^^^^^^^^^^^^^^^^^^^
Some problems are dealing with supply/demand in one form or another. From the information the LLM has been trained on,
it might be prone to assume that supply and demand should be equal. Since this is often not the case, this can be a
too strict of an assumption and could cause the model to become infeasible.

For instance, the following problem (partially shown):

.. code-block:: console

   Imagine you are coordinating a logistics effort to redistribute essential supplies among seven regional distribution centers. Each center starts with a specific quantity of supplies but has different needs to ensure smooth operations across the regions.

   Here's the initial setup:

   - Distribution Center 1 has 97 units but needs 119 units.
   - Distribution Center 2 has 458 units but needs 275 units.
   - Distribution Center 3 has 473 units but needs only 36 units.

   ...

The LLM might propose the following constraint:

.. epigraph::

    **Constraints:**

    1. Balance constraints: The amount of supplies in each region after transfers should be equal to the demand.

    .. math::

        \sum_{j=1}^{7} x_{ij} - \sum_{j=1}^{7} x_{ji} = s_i - d_i \quad \forall i \in \{1, \ldots, 7\}

Even if you cannot read the equation, the description describes what it does: it assumes that supply and demand are
perfectly balanced. This means that if there is more supply than demand, the model will be infeasible. The above can be
fixed by making the following change:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Your task is to ensure each distribution center has the supplies it needs while minimizing the total cost of redistribution.
         What would be the minimum cost to achieve this?

         ...


   .. tab:: Good

      .. code-block:: text

         Your task is to ensure each distribution center has the supplies it needs while minimizing the total cost of redistribution.
         What would be the minimum cost to achieve this? Note that supply and demand are not equal.

         ...

Avoid abstract concepts
^^^^^^^^^^^^^^^^^^^^^^^
TODO: It cannot think in 3D.
