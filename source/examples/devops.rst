DevOps Engineer
===============


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


Assigning workloads
-------------------

.. image:: images/devops_assigning_workloads.png
   :alt: Assigning workloads
   :align: center

Having a limited number of machines to schedule workloads on, assign the jobs so as to
minimize the number of machines impacted.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/devops_assigning_workloads.txt
         :language: text

   .. tab:: Example generated model

      .. literalinclude:: content/devops_assigning_workloads.py
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

.. image:: images/devops_testing_strategy.png
   :alt: Testing strategy optimization
   :align: center

Smartly decide which machines to run tests on and what kind of testing environment to simulate.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/devops_testing_strategy.txt
         :language: text

   .. tab:: Data

      .. literalinclude:: content/devops_testing_strategy.csv
         :language: text

   .. tab:: Example generated model

      .. literalinclude:: content/devops_testing_strategy.py
         :language: python