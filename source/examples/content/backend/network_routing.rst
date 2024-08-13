.. raw:: html

    <h2>🔢 Problem Definition</h2>

**Decision Variables:**

- :math:`x_i`: Percentage of requests routed to Backend Service :math:`i` where :math:`i \in \{A, B, C, D, E\}`.
- :math:`y_{ij}`: Percentage of requests routed from Backend Service :math:`i` to Internal Gateway :math:`j` where :math:`j \in \{F, G, H, I, J, K, L, M, N\}` and :math:`i \in \{A, B, C, D, E\}`.

**Parameters:**

- :math:`T_i`: Average processing time of Backend Service :math:`i` (ms).
- :math:`R_i`: Reliability of Backend Service :math:`i` (%).
- :math:`C_i`: Cost per request for Backend Service :math:`i` ($).
- :math:`T_{ij}`: Additional processing time for routing from Backend Service :math:`i` to Internal Gateway :math:`j` (ms).
- :math:`R_{ij}`: Additional reliability for routing from Backend Service :math:`i` to Internal Gateway :math:`j` (%).
- :math:`C_{ij}`: Additional cost per request for routing from Backend Service :math:`i` to Internal Gateway :math:`j` ($).

**Objective:**

Minimize the total latency of the system:

.. math::

    \text{Minimize} \quad \sum_{i \in \{A, B, C, D, E\}} \left( x_i \cdot T_i + \sum_{j \in \text{Gateways reachable from } i} y_{ij} \cdot T_{ij} \right)

**Constraints:**

1. **Backend Reliability Constraint:**

   .. math::

      \sum_{i \in \{A, B, C, D, E\}} x_i \cdot R_i \geq 0.995

2. **Internal Reliability Constraint:**

   .. math::

      \sum_{i \in \{A, B, C, D, E\}} \sum_{j \in \text{Gateways reachable from } i} y_{ij} \cdot R_{ij} \geq 0.995

3. **Backend Routing Constraint:**

   .. math::

      \sum_{i \in \{A, B, C, D, E\}} x_i = 1, \quad 0 \leq x_i \leq 0.4

4. **Internal Routing Constraint:**

   .. math::

      \sum_{j \in \text{Gateways reachable from } i} y_{ij} = 1, \quad 0 \leq y_{ij} \leq 0.75 \quad \forall i \in \{A, B, C, D, E\}

5. **Cost Constraint:**

   .. math::

      \sum_{i \in \{A, B, C, D, E\}} \left( x_i \cdot C_i + \sum_{j \in \text{Gateways reachable from } i} y_{ij} \cdot C_{ij} \right) \leq 0.4

6. **Non-Negativity Constraint:**

   .. math::

      x_i \geq 0, \quad y_{ij} \geq 0
