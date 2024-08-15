.. raw:: html

    <h2>🔢 Problem Definition</h2>

We are given an investment problem where an investor needs to allocate their capital over three years among different investment projects to maximize the capital at the end of year 3.

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{i,j}`: Amount of capital invested in project :math:`j` during year :math:`i` (where :math:`i \in \{1, 2, 3\}` and :math:`j \in \{1, 2, 3, 4\}`).

.. raw:: html

    <h3>Intermediate Variables</h3>

- :math:`C_i`: Capital available at the start of year :math:`i` (where :math:`i \in \{1, 2, 3, 4\}`).

.. raw:: html

    <h3>Objective</h3>

Maximize the capital at the start of year 4, :math:`C_4`.

.. raw:: html

    <h3>Constraints</h3>

1. Initial capital at year 1: :math:`C_1 = 500,000`.
2. Capital in subsequent years:
   - :math:`C_{i+1} = \sum_{j} x_{i,j} \times (1 + r_j)`, where :math:`r_j` is the return rate of project :math:`j`.
3. Capital allocation constraints:
   - :math:`C_1 = x_{1,1} + x_{1,2}`
   - :math:`C_2 = x_{2,1} + x_{2,3}`
   - :math:`C_3 = x_{3,1} + x_{3,4}`
4. Investment constraints:
   - :math:`x_{1,2} \leq 120,000`
   - :math:`x_{2,3} \leq 150,000`
   - :math:`x_{3,4} \leq 100,000`

.. raw:: html

    <h3>Return Rates</h3>

- :math:`r_1 = 0.2` (20%)
- :math:`r_2 = 1.5` (150%)
- :math:`r_3 = 1.6` (160%)
- :math:`r_4 = 0.4` (40%)
