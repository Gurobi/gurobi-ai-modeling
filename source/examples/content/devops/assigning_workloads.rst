.. raw:: html

    <h2>Problem Definition</h2>


.. raw:: html

    <h3>Objective:</h3>

Maximize the sum of unused resources across all machines without any workloads assigned to them.

.. raw:: html

    <h3>Sets:</h3>

- **M**: Set of machines, indexed by \(m\).
- **W**: Set of workloads, indexed by \(w\).


.. raw:: html

    <h3>Parameters:</h3>

For each machine \(m\) in **M**:

- **vCPU_m**: vCPU capacity of machine \(m\).
- **RAM_m**: RAM capacity (in GB) of machine \(m\).
- **GPU_m**: GPU capacity (in GFLOPS) of machine \(m\).

For each workload \(w\) in **W**:

- **vCPU_w**: vCPU requirement of workload \(w\).
- **RAM_w**: RAM requirement (in GB) of workload \(w\).
- **GPU_w**: GPU requirement (in GFLOPS) of workload \(w\).

.. raw:: html

    <h3>Decision Variables:</h3>

- **x_mw \in \{0, 1\}**: Binary variable indicating if workload \(w\) is assigned to machine \(m\).
- **y_m \in \{0, 1\}**: Binary variable indicating if machine \(m\) has no workloads assigned to it.

.. raw:: html

    <h3>Updated Objective:</h3>

Maximize the total unused resources across all machines without any workloads assigned:

.. math::

   \text{Maximize} \quad \sum_{m \in M} y_m \cdot (\text{vCPU}_m + \text{RAM}_m + \text{GPU}_m)

.. raw:: html

    <h3>Constraints:</h3>

1. **vCPU Capacity**:

   .. math::

      \sum_{w \in W} x_{mw} \cdot \text{vCPU}_w \leq \text{vCPU}_m \quad \forall m \in M

2. **RAM Capacity**:

   .. math::

      \sum_{w \in W} x_{mw} \cdot \text{RAM}_w \leq \text{RAM}_m \quad \forall m \in M

3. **GPU Capacity**:

   .. math::

      \sum_{w \in W} x_{mw} \cdot \text{GPU}_w \leq \text{GPU}_m \quad \forall m \in M

4. **All Workloads Must be Scheduled**:

   .. math::

      \sum_{m \in M} x_{mw} = 1 \quad \forall w \in W

5. **Unused Machine Condition**:

   .. math::

      \sum_{w \in W} x_{mw} \leq (1 - y_m) \times |W| \quad \forall m \in M

   This ensures that if a machine has any workload assigned (\(\sum_{w} x_{mw} > 0\)), then \(y_m\) is forced to 0, meaning the machine is considered used.
