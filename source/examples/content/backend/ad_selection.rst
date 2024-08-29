.. raw:: html

    <h2>🔢 Problem Definition</h2>

.. raw:: html

    <h3>Sets</h3>

- :math:`P`: Set of pages :math:`p`.
- :math:`A`: Set of ads :math:`a`.

.. raw:: html

    <h3>Parameters</h3>

- :math:`\text{CTR}_{p,a}`: Click-Through Rate of ad :math:`a` on page :math:`p` (in percentage).
- :math:`\text{Revenue}_{a}`: Revenue generated per click from ad :math:`a` (in dollars).
- :math:`\text{InterestMatch}_{a}`: Binary parameter indicating if ad :math:`a` matches user interests (1 if Yes, 0 if No).
- :math:`\text{Cost}_{a}`: Cost per ad :math:`a` (in dollars).
- :math:`\text{MaxAdsPerPage} = 3`: Maximum number of ads per page.
- :math:`\text{MinCTR} = 2.5`: Minimum average CTR across all selected ads.
- :math:`\text{BudgetLimit} = 500`: Maximum budget for the cost of selected ads.

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{p,a}`: Binary decision variable, 1 if ad :math:`a` is selected for page :math:`p`, 0 otherwise.

.. raw:: html

    <h3>Objective</h3>

Maximize the total revenue across all pages:

.. math::

    \text{Maximize} \quad Z = \sum_{p \in P} \sum_{a \in A} \text{Revenue}_{a} \times \text{CTR}_{p,a} \times x_{p,a}

.. raw:: html

    <h3>Constraints</h3>

1. **Overall CTR Constraint**:

.. math::

    \frac{\sum_{p \in P} \sum_{a \in A} \text{CTR}_{p,a} \times x_{p,a}}{\sum_{p \in P} \sum_{a \in A} x_{p,a}} \geq 2.5

2. **Page CTR Constraint**:
   For each page :math:`p`:

.. math::

    \text{If } x_{p,a} = 1 \text{ and } \text{CTR}_{p,a} < 2.0\%, \text{ then there exists } x_{p,a'} = 1 \text{ with } \text{CTR}_{p,a'} > 3.0\%

3. **User Experience Constraint**:

.. math::

    \sum_{a \in A} x_{p,a} \leq 3 \quad \forall p \in P

4. **Relevance Constraint**:

.. math::

    \sum_{p \in P} \sum_{a \in A} \text{InterestMatch}_{a} \times x_{p,a} \geq 0.7 \times \sum_{p \in P} \sum_{a \in A} x_{p,a}

5. **Budget Constraint**:

.. math::

    \sum_{p \in P} \sum_{a \in A} \text{Cost}_{a} \times x_{p,a} \leq 500