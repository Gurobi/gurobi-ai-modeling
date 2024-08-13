.. raw:: html

    <h2>🔢 Problem Definition</h2>

In this problem, we are tasked with optimizing pricing strategies for a range of electronic products to maximize the total revenue. The optimization problem can be defined as follows:

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`P_i`: Price of product :math:`i`

.. raw:: html

    <h3>Parameters</h3>

- :math:`S_i`: Stock Quantity of product :math:`i`
- :math:`Q0_i`: Base Demand for product :math:`i`
- :math:`P0_i`: Base Price for product :math:`i`
- :math:`W_i`: Weight (kg) of product :math:`i`
- :math:`Z_i`: Size (kg) of product :math:`i`
- :math:`BSC_i`: Base Shipping Cost for product :math:`i`
- :math:`E_i`: Price Elasticity for product :math:`i`

.. raw:: html

    <h3>Objective Function</h3>

The objective is to maximize the total revenue:

.. math::

   \text{Maximize } \sum_{i} \left(P_i \times Q_i - \left(BSC_i + (2 \times Z_i + 1.5 \times W_i) \times Q_i\right)\right)

Where :math:`Q_i` (the demand for product :math:`i`) is given by the demand elasticity equation:

.. math::

   Q_i = Q0_i \times \left(1 - E_i \times \frac{(P_i - P0_i)}{P0_i}\right)

.. raw:: html

    <h3>Constraints</h3>

1. **Stock Availability**: The total quantity of each product sold cannot exceed the available stock.

   .. math::

      Q_i \leq S_i \quad \forall i

2. **Minimum Price Constraint**: Prices must be at least 80% of the base price.

   .. math::

      P_i \geq 0.8 \times P0_i \quad \forall i

3. **Non-negative Demand**: Ensure that demand remains non-negative.

   .. math::

      Q_i \geq 0 \quad \forall i