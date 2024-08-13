.. raw:: html

    <h2>🔢 Problem Definition</h2>

We want to minimize the total cost of a diet while meeting specific dietary constraints. The mathematical model is defined as follows:

**Decision Variables**:
  Let :math:`x_i` be the number of portions of food item :math:`i` consumed, where :math:`i` belongs to the set of available food items. Since portions are non-divisible, :math:`x_i` must be an integer.

**Parameters**:
  - :math:`c_i`: cost of one portion of food item :math:`i`
  - :math:`cal_i`: calories in one portion of food item :math:`i`
  - :math:`p_i`: protein content in one portion of food item :math:`i`
  - :math:`f_i`: fat content in one portion of food item :math:`i`
  - :math:`s_i`: sodium content in one portion of food item :math:`i`

**Objective Function**:
  Minimize the total cost:

  .. math::

      \text{Minimize } \sum_{i} c_i \cdot x_i

**Constraints**:

1. **Caloric intake between 1800 and 2200 calories**:

   .. math::

      1800 \leq \sum_{i} cal_i \cdot x_i \leq 2200

2. **Protein intake at least 91 grams**:

   .. math::

      \sum_{i} p_i \cdot x_i \geq 91

3. **Fat intake at most 65 grams**:

   .. math::

      \sum_{i} f_i \cdot x_i \leq 65

4. **Sodium intake at most 1779 mg**:

   .. math::

      \sum_{i} s_i \cdot x_i \leq 1779

5. **Non-divisible portions**:

   .. math::

      x_i \in \mathbb{Z}_+ \quad \text{(non-negative integers)}
