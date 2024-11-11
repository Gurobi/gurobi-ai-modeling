Write problems as unambiguous as possible
-----------------------------------------
As human beings, we often make a similar mistake in our casual and business interactions: assuming the other party holds the same definition of the
words we use. Such a semantic conflict can cause confusion when you send somebody on an errand and the person comes back
with something else than you had expected. Humans often have procedures for this by asking clarifying questions:
`what exactly do you mean by ...?`. Unfortunately, the current generation of LLMs does not seem to express the degree
of confusion under which they are generating a response, leading it to just make assumptions about what you mean.

Currently the only way of dealing with this is by making sure your prompt is as unambiguous as possible.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Minimize energy consumption.

   .. tab:: Good

      .. code-block:: text

         Minimize the total energy consumption of all production facilities, defined as the sum of electricity, fuel, and water usage.

Or to bring it into the domain of Software Engineers:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to deploy 5 applications on AWS using either EC2 and/or Fargate, but minimizing costs.
         Each application has specific CPU and RAM requirements, and you need to decide whether to deploy them on AWS EC2 instances or Fargate.

         Objective: Minimize total deployment cost

   .. tab:: Good

      .. code-block:: text

         I want to deploy 5 applications on AWS using either EC2 and/or Fargate, but minimizing costs.

         Objective: Minimize total monthly deployment costs.

         Constraints:
         - There should be 1 of every application.
         For EC2 instances:
           - One EC2 instance can run multiple Apps
           - The combined vCPU and RAM usage cannot exceed a single EC2 instance's capability
           - You can instantiate multiple EC2 instances of the same type
         For Fargate instances:
           - One Fargate instance can only run one App
           - The vCPU and RAM usage cannot exceed the Fargate instance capability
           - You can instantiate multiple Fargate instances of the same type