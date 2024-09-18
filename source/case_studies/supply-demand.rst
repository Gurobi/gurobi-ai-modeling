I blindly assume that supply and demand are equal
=================================================

.. include:: /_static/feedback.rst

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

