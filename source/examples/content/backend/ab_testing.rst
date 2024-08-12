.. raw:: html

    <h2>🔢 Problem Definition</h2>

Let's define the problem as follows:

.. raw:: html

    <h3>Sets</h3>

- **S**: Set of user segments, where S = {New Users, Regular Users, Power Users}.
- **V**: Set of variants, where V = {V1, V2, ..., V10}.

.. raw:: html

    <h3>Parameters</h3>

- **U_s**: Total number of users in segment *s* ∈ S.
- **D_{s,v}**: Disruption for user segment *s* with variant *v*.

.. raw:: html

    <h3>Decision Variables</h3>

- **x_v**: Binary variable indicating whether variant *v* is selected (x_v = 1) or not (x_v = 0).
- **y_{s,v}**: Number of users in segment *s* allocated to variant *v*.

.. raw:: html

    <h3>Objective</h3>

Minimize the total disruption:

.. math::

   \text{Minimize} \quad \sum_{s \in S} \sum_{v \in V} D_{s,v} \cdot y_{s,v}

.. raw:: html

    <h3>Constraints</h3>

1. **Selection Constraint**: Choose exactly 3 out of 10 possible variants:

   .. math::

      \sum_{v \in V} x_v = 3

2. **Minimum Users Constraint**: Each chosen variant must have at least 100 users in each user segment:

   .. math::

      y_{s,v} \geq 100 \times x_v, \quad \forall s \in S, v \in V

3. **Total Users Constraint**: Make sure all users from each segment are allocated:

   .. math::

      \sum_{v \in V} y_{s,v} = U_s, \quad \forall s \in S

4. **Balance Constraint**: Within each user segment, the difference of allocation between any two chosen variants cannot be more than 300:

   .. math::

      y_{s,v_1} - y_{s,v_2} \leq 300, \quad \forall s \in S, v_1 \in V, v_2 \in V

   .. math::

      y_{s,v_2} - y_{s,v_1} \leq 300, \quad \forall s \in S, v_1 \in V, v_2 \in V
