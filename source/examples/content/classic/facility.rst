.. raw:: html

    <h2>🔢 Problem Definition</h2>

We need to determine which plant(s) should be closed to minimize the total costs, which include both transportation costs and fixed costs associated with keeping plants open. The problem can be formulated as a Mixed-Integer Linear Programming (MILP) problem.

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{ij}`: Amount of products shipped from plant :math:`i` to warehouse :math:`j` (continuous variable)
- :math:`y_i`: Binary variable indicating whether plant :math:`i` is open (1 if open, 0 if closed)

.. raw:: html

    <h3>Parameters</h3>

- :math:`c_{ij}`: Transportation cost per 1000 products from plant :math:`i` to warehouse :math:`j`
- :math:`f_i`: Fixed cost of keeping plant :math:`i` open
- :math:`d_j`: Demand at warehouse :math:`j`
- :math:`s_i`: Capacity of plant :math:`i`

.. raw:: html

    <h3>Objective Function</h3>

Minimize the total cost, which is the sum of the transportation costs and the fixed costs for the open plants:

.. math::

    \text{Minimize } \sum_{i=1}^{5} \sum_{j=1}^{4} c_{ij} \cdot x_{ij} + \sum_{i=1}^{5} f_i \cdot y_i

.. raw:: html

    <h3>Constraints</h3>

1. **Demand fulfillment**: The total products shipped to each warehouse must meet the demand.

.. math::

    \sum_{i=1}^{5} x_{ij} = d_j \quad \forall j \in \{1, 2, 3, 4\}

2. **Capacity constraints**: The total products shipped from each plant must not exceed its capacity and can only ship if the plant is open.

.. math::

    \sum_{j=1}^{4} x_{ij} \leq s_i \cdot y_i \quad \forall i \in \{1, 2, 3, 4, 5\}

3. **Non-negativity and binary constraints**:

.. math::

    x_{ij} \geq 0 \quad \forall i \in \{1, 2, 3, 4, 5\}, \, \forall j \in \{1, 2, 3, 4\}

.. math::

    y_i \in \{0, 1\} \quad \forall i \in \{1, 2, 3, 4, 5\}
