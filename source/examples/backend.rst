.. _examples_backend:

Backend Engineer
================

Ad Selection
------------

.. image:: images/backend_ad_selection.png
   :alt: Ad Selection
   :align: center

Select which ads should be run on your website to maximize revenue, taking into account the associated cost and user experience.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/backend/ad_selection.txt
         :language: text

   .. tab:: Data

      :download:`ad_selection.csv: <content/backend/ad_selection.csv>`

      .. literalinclude:: content/backend/ad_selection.csv
         :language: text

   .. tab:: Generated Model formulation

      .. include:: content/backend/ad_selection.rst

   .. tab:: Generated Python code

      .. literalinclude:: content/backend/ad_selection.py
         :language: python

A/B Testing
----------------------

.. image:: images/backend_ab_testing.png
   :alt: A/B Testing
   :align: center

Choose from a pool of A/B variants and allocate different user segments to them to minimize user disruption while
upholding statistical significance.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/backend/ab_testing.txt
         :language: text

   .. tab:: Data

      :download:`ab_testing.csv: <content/backend/ab_testing.csv>`

      .. literalinclude:: content/backend/ab_testing.csv
         :language: text

   .. tab:: Generated Model formulation

      .. include:: content/backend/ab_testing.rst

   .. tab:: Generated Python code

      .. literalinclude:: content/backend/ab_testing.py
         :language: python

Backend API Routing
-------------------

.. image:: images/backend_network_routing.png
   :alt: Backend API Routing
   :align: center

Route the network from end-users to first and second-degree internal servers, minimizing latency while maintaining low cost and a reliability SLA.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/backend/network_routing.txt
         :language: text

   .. tab:: Data

      :download:`network_routing_backend.csv: <content/backend/network_routing_backend.csv>`

      .. literalinclude:: content/backend/network_routing_backend.csv
         :language: text

      :download:`network_routing_internal.csv: <content/backend/network_routing_internal.csv>`

      .. literalinclude:: content/backend/network_routing_internal.csv
         :language: text

   .. tab:: Generated Model formulation

      .. include:: content/backend/network_routing.rst

   .. tab:: Generated Python code

      .. literalinclude:: content/backend/network_routing.py
         :language: python

E-Commerce Pricing
-------------------

.. image:: images/backend_ecommerce.png
   :alt: Backend API Routing
   :align: center

Determine the optimal sales price for the items on an E-commerce platform.

.. tabs::

   .. tab:: Prompt

      .. literalinclude:: content/backend/ecommerce.txt
         :language: text

   .. tab:: Data

      :download:`ecommerce.csv: <content/backend/ecommerce.csv>`

      .. literalinclude:: content/backend/ecommerce.csv
         :language: text

   .. tab:: Generated Model formulation

      .. include:: content/backend/ecommerce.rst

   .. tab:: Generated Python code

      .. literalinclude:: content/backend/ecommerce.py
         :language: python
