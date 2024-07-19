DevOps Engineer
===============

Assigning workloads
-------------------

Having a limited number of machines to schedule workloads on, assign the jobs so as to
minimize the number of machines impacted.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/devops_assigning_workloads.txt
         :language: text

   .. tab:: Example generated model

      .. literalinclude:: content/devops_assigning_workloads.py
         :language: python



Scheduling deployments
----------------------

.. image:: images/devops_scheduling_deployments.png
   :alt: Scheduling deployments
   :align: center

Schedule resource-heavy deployments on customer-facing hardware at low-traffic times so
that customers are least likely to be impacted.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/devops_scheduling_deployments.txt
         :language: text

   .. tab:: Example generated model

      .. literalinclude:: content/devops_scheduling_deployments.py
         :language: python


Incident Response Planning
-------------------------------------

.. image:: images/devops_incident_response.png
   :alt: Disaster Recovery Planning
   :align: center

A complex system of internal and customer-facing services that have many interdependencies
should be brought online efficiently in case of a disaster. The customer-facing services
get assigned a priority value, determine the order in which the services should be brought
back online.

To induce urgency, we utilize the following formula that states that customer-facing services
should be brought online as quickly as possible, with more important services getting a higher priority:

:math:`V(t) = V_0 \cdot e^{-0.0398t}`


.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/devops_incident_response.txt
         :language: text

   .. tab:: Data

      .. literalinclude:: content/devops_incident_response.json
         :language: json

   .. tab:: Example generated model

      .. literalinclude:: content/devops_incident_response.py
         :language: python


.. _testing_strategy:

Testing strategy optimization
-----------------------------

Smartly decide which machines to run tests on and what kind of testing environment to simulate.

The prompt to generate a working model could look as follows:

.. code-block:: console

   You are tasked with optimizing the testing strategy for your company's continuous integration and continuous delivery (CI/CD) pipeline. Your goal is to select 5 machines to run tests on in a way that maximizes the coverage of different test environments while prioritizing machines that have not been tested on recently. Also take into account that if a machine did not pass the test last time it should be prioritized. Below is the dataset of previous test results and the mapping of machines to available test environments.

   Dataset: Previous Test Results
   machine	test_timestamp	passed	test_environment_tested
   M1	2024-05-01 14:00	1	EnvA
   M2	2024-05-01 14:30	0	EnvB
   M3	2024-05-01 15:00	1	EnvA
   M4	2024-05-01 15:30	1	EnvC
   M5	2024-05-01 16:00	0	EnvA
   M1	2024-05-02 10:00	1	EnvB
   M2	2024-05-02 10:30	1	EnvC
   M3	2024-05-02 11:00	0	EnvB
   M6	2024-05-02 11:30	1	EnvC
   M7	2024-05-02 12:00	0	EnvA
   M8	2024-05-02 12:30	1	EnvB
   M9	2024-05-02 13:00	1	EnvC
   M10	2024-05-02 13:30	0	EnvA
   M11	2024-05-02 14:00	1	EnvB
   M12	2024-05-02 14:30	0	EnvC
   M13	2024-05-02 14:30	0	EnvC
   M14	2024-05-02 14:30	0	EnvC
   M15	2024-05-02 14:30	0	EnvC

   Mapping: Machines to Available Test Environments
   machine	test_environments
   M1	EnvA, EnvB
   M2	EnvB, EnvC
   M3	EnvA, EnvB, EnvC
   M4	EnvC
   M5	EnvA
   M6	EnvC
   M7	EnvA, EnvB
   M8	EnvB, EnvC
   M9	EnvC
   M10	EnvA
   M11	EnvB
   M12	EnvC
   M13	EnvA, EnvB
   M14	EnvB, EnvC
   M15	EnvA

   Objective:

   Select 5 machines to run the next set of tests. Your selection should:

       Maximize the coverage of different test environments (EnvA, EnvB, EnvC).
       Prioritize machines that have not been tested on recently (considering the latest test_timestamp).
       Prioritize machines on which the test did not pass last time