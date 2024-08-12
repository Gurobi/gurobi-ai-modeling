.. raw:: html

    <h2>🔢 Problem Definition</h2>

**Objective: Maximize Revenue**

.. raw:: html

    <h3>Sets and Indices</h3>

- :math:`P`: Set of pages.
- :math:`A_p`: Set of ads available for page :math:`p`.
- :math:`i`: Index for ads.
- :math:`p`: Index for pages.

.. raw:: html

    <h3>Parameters</h3>

- :math:`\text{CTR}_i`: Click-Through Rate (CTR) of ad :math:`i`.
- :math:`\text{Rev}_i`: Revenue per click for ad :math:`i`.
- :math:`\text{Cost}_i`: Cost per display of ad :math:`i`.
- :math:`\text{InterestMatch}_i`: 1 if the ad :math:`i` matches user interests, 0 otherwise.
- :math:`B`: Budget constraint for total cost, set at $500.
- :math:`\text{MinCTR}`: Minimum overall CTR requirement (2.5%).
- :math:`\text{HighCTRThreshold}`: Threshold for high CTR ads (3.0%).
- :math:`\text{LowCTRThreshold}`: Threshold for low CTR ads (2.0%).
- :math:`\text{MaxAdsPerPage}`: Maximum number of ads per page (3).
- :math:`\text{RelevanceThreshold}`: Minimum percentage of relevant ads (70%).

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{i,p}`: Binary variable, 1 if ad :math:`i` is selected for page :math:`p`, 0 otherwise.

.. raw:: html

    <h3>Objective</h3>

Maximize the total revenue:

.. math::
   \text{Maximize } \sum_{p \in P} \sum_{i \in A_p} x_{i,p} \cdot \text{CTR}_i \cdot \text{Rev}_i

.. raw:: html

    <h3>Constraints</h3>

1. **Overall CTR Constraint**:

   .. math::
      \frac{\sum_{p \in P} \sum_{i \in A_p} x_{i,p} \cdot \text{CTR}_i}{\sum_{p \in P} \sum_{i \in A_p} x_{i,p}} \geq \text{MinCTR}

2. **Page CTR Constraint**:
   For each page :math:`p`:

   .. math::
      \text{If } \sum_{i \in A_p, \text{CTR}_i < \text{LowCTRThreshold}} x_{i,p} \geq 1, \text{ then } \sum_{i \in A_p, \text{CTR}_i \geq \text{HighCTRThreshold}} x_{i,p} \geq 1

3. **Page Ad Constraint**:
   Each ad can only be shown on pages where it is mapped:

   .. math::
      x_{i,p} \leq 1 \quad \forall p, \forall i \in A_p

4. **User Experience Constraint**:
   A maximum of 3 ads per page:

   .. math::
      \sum_{i \in A_p} x_{i,p} \leq \text{MaxAdsPerPage} \quad \forall p

5. **Relevance Constraint**:
   At least 70% of the ads must match user interests:

   .. math::
      \frac{\sum_{p \in P} \sum_{i \in A_p} x_{i,p} \cdot \text{InterestMatch}_i}{\sum_{p \in P} \sum_{i \in A_p} x_{i,p}} \geq \text{RelevanceThreshold}

6. **Budget Constraint**:
   The total cost of ads displayed must not exceed $500 per day:

   .. math::
      \sum_{p \in P} \sum_{i \in A_p} x_{i,p} \cdot \text{Cost}_i \leq B
