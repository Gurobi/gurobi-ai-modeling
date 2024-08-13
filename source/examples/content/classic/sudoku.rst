.. raw:: html

    <h2>🔢 Problem Definition</h2>

A Sudoku puzzle is a 9x9 grid divided into nine 3x3 subgrids, where each row, column, and subgrid must contain the digits 1 through 9 exactly once. The problem is to fill in the missing digits (represented by periods in the input) while satisfying these constraints.

Let :math:`x_{i,j,k}` be a binary variable that is 1 if the cell :math:`(i,j)` contains the digit :math:`k`, and 0 otherwise.

**Objective:**

Minimize 0 (this is a feasibility problem, so there is no objective function to minimize).

**Constraints:**

1. Each cell :math:`(i,j)` must contain exactly one digit:

   .. math::
      \sum_{k=1}^{9} x_{i,j,k} = 1 \quad \forall i,j

2. Each digit :math:`k` must appear exactly once in each row :math:`i`:

   .. math::
      \sum_{j=1}^{9} x_{i,j,k} = 1 \quad \forall i,k

3. Each digit :math:`k` must appear exactly once in each column :math:`j`:

   .. math::
      \sum_{i=1}^{9} x_{i,j,k} = 1 \quad \forall j,k

4. Each digit :math:`k` must appear exactly once in each 3x3 subgrid:

   .. math::
      \sum_{i \in S_r, j \in S_c} x_{i,j,k} = 1 \quad \forall k, \text{ for each } 3 \times 3 \text{ subgrid } S_r \times S_c

Given the input grid, certain variables :math:`x_{i,j,k}` will be fixed to 1 based on the known digits.
