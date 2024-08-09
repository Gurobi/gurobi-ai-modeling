.. raw:: html

    <h2>Mathematical Formulation</h2>

Let :math:`T` be the total number of time periods in the day.

- :math:`L_t` is the customer load at time :math:`t`.
- :math:`D_i` is the deployment load for deployment :math:`i`.
- :math:`C_i` is the duration of deployment :math:`i`.
- :math:`S_i` is the start time of deployment :math:`i`.
- :math:`x_{i,t}` is a binary variable indicating whether deployment :math:`i` is running at time :math:`t`.

.. raw:: html

    <h3>Objective</h3>

We aim to minimize the maximum deviation from the average load:

.. math::

   \text{Minimize} \quad \text{max_deviation}

Where

.. math::

   \text{max_deviation} \geq \left( \sum_{i} \sum_{k=0}^{C_i-1} D_i \cdot x_{i,t-k} + L_t - \frac{1}{T} \sum_{t=0}^{T} \left(L_t + \sum_{i} D_i \cdot C_i\right) \right)

.. raw:: html

    <h3>Constraints</h3>

1. **Deployment Window Constraints**:

   Each deployment :math:`i` must start within its allowed time window:

   .. math::

      S_i \in [\text{Deployment Start Window Start}_i, \text{Deployment Start Window End}_i]

2. **Non-preemptive Constraint**:

   Once a deployment starts, it must run for its full duration:

   .. math::

      \sum_{t=\text{Start Window Start}_i}^{\text{Start Window End}_i} x_{i,t} = 1

3. **Load Capacity Constraint**:

   The total load at any time :math:`t` must not exceed the server capacity:

   .. math::

      \sum_{i} \sum_{k=0}^{C_i-1} D_i \cdot x_{i,t-k} + L_t \leq 100 \quad \forall t
