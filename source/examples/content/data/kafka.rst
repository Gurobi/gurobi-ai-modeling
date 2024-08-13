.. raw:: html

    <h2>🔢 Problem Definition</h2>

Given the data on brokers, topics, and transfer rates, we need to define the following optimization problem:

.. raw:: html

    <h3>Sets</h3>

- **B**: Set of brokers, indexed by :math:`b`.
- **T**: Set of topics, indexed by :math:`t`.

.. raw:: html

    <h3>Parameters</h3>

- :math:`\text{MaxPartitions}_b`: Maximum number of partitions that broker :math:`b` can handle.
- :math:`\text{MinPartitions}_t`: Minimum number of partitions for topic :math:`t`.
- :math:`\text{MaxPartitions}_t`: Maximum number of partitions for topic :math:`t`.
- :math:`\text{TransferRate}_{b1,b2}`: Transfer rate from broker :math:`b1` to broker :math:`b2`.

.. raw:: html

    <h3>Decision Variables</h3>

- :math:`x_{t,b}`: Number of partitions of topic :math:`t` assigned to broker :math:`b`.

.. raw:: html

    <h3>Objective</h3>

Maximize throughput by minimizing data transfer between brokers. This can be achieved by minimizing the total data transfer cost across all brokers:

.. math::

    \text{Minimize } \sum_{t \in T} \sum_{b1 \in B} \sum_{b2 \in B} \text{TransferRate}_{b1,b2} \cdot x_{t,b1} \cdot x_{t,b2}

.. raw:: html

    <h3>Constraints</h3>

1. **Partition Capacity Constraint**: The number of partitions assigned to each broker must not exceed the broker's maximum capacity.

   .. math::

      \sum_{t \in T} x_{t,b} \leq \text{MaxPartitions}_b, \quad \forall b \in B

2. **Topic Partition Constraint**: The number of partitions assigned to each topic must lie within the specified range.

   .. math::

      \text{MinPartitions}_t \leq \sum_{b \in B} x_{t,b} \leq \text{MaxPartitions}_t, \quad \forall t \in T

3. **Broker Load Balance Constraint**: The total number of partitions assigned to each broker should be as balanced as possible, with no broker deviating more than 20% from the broker average.

   .. math::

      \sum_{t \in T} x_{t,b} \leq 1.2 \cdot \frac{\sum_{t \in T} \sum_{b \in B} x_{t,b}}{|B|}, \quad \forall b \in B

      \sum_{t \in T} x_{t,b} \geq 0.8 \cdot \frac{\sum_{t \in T} \sum_{b \in B} x_{t,b}}{|B|}, \quad \forall b \in B

4. **Partition Distribution Constraint**: For each topic, no broker can hold more than 40% of the partitions.

   .. math::

      x_{t,b} \leq 0.4 \cdot \sum_{b \in B} x_{t,b}, \quad \forall t \in T, \forall b \in B
