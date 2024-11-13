Use cases
=========

Optimization problems can be seen virtually everywhere if you look for
them, and many of these problems can actually be solved once you model them.
In the introduction we mentioned that this documentation mainly focuses on Software
Engineers. The reason for this is a practical one: if you have tried to explain or have somebody explain optimization to
you, you might know that it can be an abstract topic. By focussing on a single professional domain we can be very
concrete about the examples and materials, taking this topic out of the abstract world and applying it to practical,
everyday problems.

Do keep in mind that the examples we came up with are use cases to illustrate a point, they might not be applicable in
their current format: they exist so that users new to optimization will have
a better idea of what to look for and how to
apply this technique to a problem that they face.

.. note::
   Not only **can** optimization be applied in the software engineering domain, it **is** being applied... by us! For
   :ref:`example <testing_strategy>`, in our CI/CD process we utilize optimization to smartly select which machines
   to run tests on and which kinds of testing environments to set up.
   So we are using Gurobi to optimize the development process at Gurobi!


Specialties
-----------

DevOps Engineer
^^^^^^^^^^^^^^^
As a DevOps Engineer you are likely encountering optimization problems on a frequent basis. Resources, be it cloud or
on-prem, are never infinite as they can be constrained by, for instance, cost or availability.

Mixed-Integer Programming (MIP) and Linear Programming (LP) models can help enhance resource allocation,
task scheduling, and overall system performance, leading to more efficient CI/CD pipelines and cost-effective cloud
resource management. For instance, think about the following questions:

- When can I best apply updates or schedule deployments while minimally impacting users?
- How should I schedule workloads on heterogeneous machines if I want to impact as few machines as possible?
- For incident response planning, which machines should get priority based on whether they are customer-facing or have dependencies?
- To optimally test our application, which parameters should I set to maximize our testing coverage?

See our :doc:`DevOps Engineer prompts <examples/devops>` for concrete examples.

Backend Engineer
^^^^^^^^^^^^^^^^
Backend and Full-Stack Engineers are operating in an environment that can be constrained from a resource perspective
but also has low-latency or other application-specific requirements.

Optimization techniques like Mixed-Integer Programming (MIP) and Linear Programming (LP) can play a role in improving API performance, application optimization and help
drive more traffic. Consider the following scenarios:

- I want to maximize ad revenue from my website, while minimizing impact on user experience.
- How can I best schedule A/B testing to different user segments to yield statistically significant results while minimizing user disruption?
- In our multi-layered microservice application, how can I route the traffic so as to minimize latency and cost?
- How do we apply dynamic pricing on our E-commerce platform based on stock and demand to maximize revenue?

See our :doc:`Backend Engineer prompts <examples/backend>` for concrete examples.

Data Engineer
^^^^^^^^^^^^^
As a Data Engineer, you're often dealing with large-scale data pipelines, data storage, and ETL (Extract, Transform, Load) processes that can be complex and resource-intensive.
Optimization in this domain can lead to significant improvements in data processing times, cost-efficiency, and overall system reliability.

Techniques like Mixed-Integer Programming (MIP) and Linear Programming (LP) can be leveraged to streamline data operations, ensuring that data flows smoothly and efficiently through your systems. Consider these optimization opportunities:

- How can I optimize the scheduling of Apache Spark batch jobs to ensure minimal downtime and efficient use of processing resources?
- What is the best way to allocate storage across various data warehouses to balance cost and retrieval speed?
- How can I design data partitioning strategies to reduce query latency while minimizing storage costs?
- For data streaming workloads as with Apache Kafka, how should I allocate topic partitions to minimize latency between brokers?

See our :doc:`Data Engineer prompts <examples/data>` for concrete examples.

.. _usecase_other:

Professions outside of the Software Engineering domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Even though this repository is primarily aimed at Software Engineers, don't let preconceived notions inhibit you.
Optimization can be applied in many ways that nobody has yet thought of!

Below are a few professions with applications to illustrate the wide range of potential applications:

- **Fitness Coaches**: Fitness coaches can use optimization to design personalized workout plans. By optimizing exercise routines based on individual goals, fitness levels, and available time, they can help clients achieve their fitness objectives more efficiently.
- **Real Estate Developers**: Real estate developers can use optimization to determine the best use of land plots. By considering factors like zoning laws, market demand, and construction costs, they can maximize the return on investment for a given property.
- **Mechanical Engineers**: Mechanical engineers can use optimization for component design. By optimizing the design parameters of mechanical parts (e.g., minimizing weight while ensuring strength), they can improve performance and reduce material costs.
- **E-commerce Managers**: E-commerce managers can use optimization for dynamic pricing and inventory management. By optimizing prices based on demand and inventory levels, they can maximize revenue and minimize stockouts or overstock situations.
- **Farmers**: Farmers can use optimization for crop rotation and planting schedules. By optimizing the sequence and timing of planting different crops, they can improve soil health and maximize yields.
- **Green Energy Consultants**: Consultants can use optimization for designing renewable energy systems. By optimizing the placement and capacity of solar panels or wind turbines, they can maximize energy production and minimize costs.
- **Television Network Schedulers**: Network schedulers can use optimization to determine the best time slots for different shows. By optimizing the broadcast schedule based on viewer ratings and advertising revenue, they can maximize audience engagement and profits.
- **Electrical Engineers**: Electrical engineers can use optimization for circuit design. By optimizing the values of components in an electrical circuit, they can achieve desired performance characteristics such as minimizing power consumption or maximizing signal integrity. By optimizing the arrangement of these components, they can design a circuit that's faster to produce.
