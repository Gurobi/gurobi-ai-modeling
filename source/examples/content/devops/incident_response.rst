.. raw:: html

    <h2>🔢 Problem Definition</h2>

**Objective**:
    Maximize the total value of the recovered systems over time, where the value of each system at the time :math:`t` is given by the function:

    .. math::

        V(t) = V_0 \cdot e^{-0.0398t}

    Here:
    
    - :math:`V_0` is the initial priority score of the system.
    - :math:`t` is the time when the system finishes recovering.

**Decision Variables**:
    
    - :math:`S_i`: The start time of recovery for system :math:`i` (continuous).
    - :math:`F_i`: The finish time of recovery for system :math:`i` (continuous).
    - :math:`V_i(t)`: The value of system :math:`i` at its finish time (continuous).

**Constraints**:

    1. **Dependency Constraints**:
    
        A system :math:`i` can only start its recovery after all its dependent systems :math:`j` have finished recovering.

        .. math::

            S_i \geq F_j \quad \forall j \in \text{Dependencies}(i)

    2. **Recovery Time Calculation**:
    
        The finish time for system :math:`i` is the start time plus its recovery duration :math:`T_i`.

        .. math::

            F_i = S_i + T_i

    3. **Piecewise Linear Approximation**:
    
        The exponential decay function :math:`e^{-0.0398t}` is approximated using a piecewise linear function over the interval of possible finish times.

**Objective Function**:

    Maximize the sum of the weighted values of all systems at their respective finish times:

    .. math::

        \text{Maximize} \sum_{i} V_0^i \cdot V_i(F_i)

    Where :math:`V_i(F_i)` is the value of the system :math:`i` at its finish time using the piecewise linear approximation of the exponential function.