.. raw:: html

    <h2>🔢 Problem Definition</h2>

We need to optimize the selection of clustering keys and materialized views to maximize the overall query performance improvement, subject to constraints on compute maintenance cost, storage cost, and ensuring a minimum total performance improvement.

.. raw:: html

    <h3>Decision Variables</h3>

Let :math:`x_i` be a binary decision variable for each query :math:`i`, where:

* :math:`x_i = 1` if we choose to optimize the query with the given clustering key or materialized view.
* :math:`x_i = 0` otherwise.

.. raw:: html

    <h3>Parameters</h3>

* :math:`c_i`: Compute maintenance cost for query :math:`i`
* :math:`s_i`: Storage cost for query :math:`i`
* :math:`p_i`: Performance improvement for query :math:`i`
* :math:`n`: Total number of queries

.. raw:: html

    <h3>Objective</h3>

Maximize the average performance improvement:

.. math::

    \text{Maximize } \frac{\sum_{i=1}^{n} p_i \cdot x_i}{n}

.. raw:: html

    <h3>Constraints</h3>

1. **Compute Maintenance Cost Constraint**: The total compute maintenance cost must not exceed 20 units.

   .. math::

       \sum_{i=1}^{n} c_i \cdot x_i \leq 20

2. **Storage Cost Constraint**: The total storage used must not exceed 45 GB.

   .. math::

       \sum_{i=1}^{n} s_i \cdot x_i \leq 45

3. **Query Performance Constraint**: Ensure at least 20% total performance improvement.

   .. math::

       \sum_{i=1}^{n} p_i \cdot x_i \geq 0.20 \times \sum_{i=1}^{n} p_i
