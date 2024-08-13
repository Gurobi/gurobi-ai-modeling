.. raw:: html

    <h2>🔢 Problem Definition</h2>

We need to assign workers to shifts while minimizing the total cost of the assignments. The problem is formulated as a mixed-integer linear program (MILP) with the following details:

.. raw:: html

    <h3>Sets</h3>

- :math:`S = \{1, 2, \dots, 14\}`: Set of shifts, where each number corresponds to a specific day (e.g., 1 = Mon1, 2 = Tue2, ..., 14 = Sun14).
- :math:`W = \{\text{Amy}, \text{Bob}, \text{Cathy}, \text{Dan}, \text{Ed}, \text{Fred}, \text{Gu}\}`: Set of workers.

.. raw:: html

    <h3>Parameters</h3>

- :math:`c_w`: Cost of assigning worker :math:`w` to a shift.

  - Amy: 10
  - Bob: 12
  - Cathy: 10
  - Dan: 8
  - Ed: 8
  - Fred: 9
  - Gu: 11

- :math:`r_s`: Number of workers required for shift :math:`s`.

  - :math:`r_1 = 3, r_2 = 2, \dots, r_{14} = 5`

- :math:`a_{w,s}`: Availability of worker :math:`w` for shift :math:`s`.

  - Binary value: 1 if worker :math:`w` is available for shift :math:`s`, 0 otherwise.

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{w,s}`: Binary variable indicating whether worker :math:`w` is assigned to shift :math:`s` (1 if assigned, 0 otherwise).

.. raw:: html

    <h3>Objective</h3>

Minimize the total cost:

.. math::

    \text{Minimize} \quad \sum_{w \in W} \sum_{s \in S} c_w \cdot x_{w,s}

.. raw:: html

    <h3>Constraints</h3>

1. **Shift Requirement**: The number of workers assigned to each shift must meet the requirement:

   .. math::

       \sum_{w \in W} x_{w,s} \geq r_s \quad \forall s \in S

2. **Availability**: A worker can only be assigned to a shift if they are available:

   .. math::

       x_{w,s} \leq a_{w,s} \quad \forall w \in W, \forall s \in S
