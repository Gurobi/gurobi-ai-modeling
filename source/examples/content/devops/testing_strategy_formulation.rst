.. raw:: html

    <h2>🔢 Problem Definition</h2>

We need to formulate an optimization problem to maximize the total score of testing a software application on four different operating systems: Linux64, Armlinux64, MacOS, and Windows. The application needs to be tested on specific machines assigned to unique testing environments.

.. raw:: html

    <h3>Objective</h3>

Maximize the total score of assigning machines to testing environments for each operating system.

.. raw:: html

    <h3>Decision Variables</h3>

Let:

-  :math:`x_{ijk}` be a binary variable that is 1 if machine  :math:`j` for OS  :math:`i` is assigned to testing environment  :math:`k`, and 0 otherwise.

.. raw:: html

    <h3>Sets</h3>

-  :math:`OS = { \text{Linux64}, \text{Armlinux64}, \text{MacOS}, \text{Windows} }`
-  :math:`E = { 1, 2, \ldots, 10 }` (testing environments)
-  :math:`M_i` is the set of machines available for OS  :math:`i`

.. raw:: html

    <h3>Parameters</h3>

-  :math:`s_{ijk}`: score for assigning machine  :math:`j` of OS  :math:`i` to testing environment  :math:`k`

.. raw:: html

    <h3>Constraints</h3>

1. Each OS must be assigned to exactly one testing environment.

.. math::
   \sum_{j \in M_i} \sum_{k \in E} x_{ijk} = 1 \quad \forall i \in OS

2. Each testing environment can be used by only one OS.

.. math::
   \sum_{i \in OS} \sum_{j \in M_i} x_{ijk} \leq 1 \quad \forall k \in E

3. Each {machine, testing environment} combination can only be chosen if the machine supports the given environment.

.. math::
   x_{ijk} \in \{0, 1\} \quad \forall i \in OS, \forall j \in M_i, \forall k \in E

.. raw:: html

    <h3>Objective Function</h3>

.. math::
   \text{Maximize} \quad \sum_{i \in OS} \sum_{j \in M_i} \sum_{k \in E} s_{ijk} x_{ijk}
