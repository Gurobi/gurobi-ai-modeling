.. raw:: html

    <h2>🔢 Problem Definition</h2>

Given a 3D tic-tac-toe board where players take turns placing X's and O's, the goal is to arrange the symbols to minimize the number of completed lines or diagonals.

.. raw:: html

    <h3>Objective</h3>

Minimize the number of completed lines or diagonals.

.. raw:: html

    <h3>Decision Variables</h3>

- Let :math:`x_{ijk}` be a binary variable where :math:`x_{ijk} = 1` if an X is placed in the cell at position :math:`(i, j, k)` on the 3D tic-tac-toe board, and 0 otherwise.
- Let :math:`o_{ijk}` be a binary variable where :math:`o_{ijk} = 1` if an O is placed in the cell at position :math:`(i, j, k)`, and 0 otherwise.

.. raw:: html

    <h3>Constraints</h3>

1. **Symbol Placement Constraint**: Each cell :math:`(i, j, k)` can contain either an X or an O, but not both:

   .. math::
      x_{ijk} + o_{ijk} = 1 \quad \forall i, j, k

2. **Total X and O Constraints**:

   .. math::
      \sum_{i=1}^{3} \sum_{j=1}^{3} \sum_{k=1}^{3} x_{ijk} = 14

   .. math::
      \sum_{i=1}^{3} \sum_{j=1}^{3} \sum_{k=1}^{3} o_{ijk} = 13

3. **Line Completion Constraints**:
   For each possible line (horizontal, vertical, and diagonal) in the 3D tic-tac-toe board, define a binary variable :math:`l` to indicate whether a line is completed. A line is completed if all three cells in that line contain the same symbol. Thus:

   .. math::
      l^X_h = 1 \text{ if a line } h \text{ is completed by X's, otherwise } l^X_h = 0

   .. math::
      l^O_h = 1 \text{ if a line } h \text{ is completed by O's, otherwise } l^O_h = 0

   Each line completion constraint would look like:

   .. math::
      l^X_h \geq x_{i_1j_1k_1} + x_{i_2j_2k_2} + x_{i_3j_3k_3} - 2

   .. math::
      l^O_h \geq o_{i_1j_1k_1} + o_{i_2j_2k_2} + o_{i_3j_3k_3} - 2

   where :math:`(i_1, j_1, k_1), (i_2, j_2, k_2), (i_3, j_3, k_3)` are the indices of the cells forming line :math:`h`.

.. raw:: html

    <h3>Objective Function</h3>

The objective is to minimize the total number of completed lines (either by X's or O's):

.. math::
   \text{Minimize} \quad \sum_{h} (l^X_h + l^O_h)
