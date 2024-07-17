I don't know how to store inventory for later use
=================================================

Similar to the previous point, our experiments have found that the current generation LLMs find it
challenging to deal with specific problems that include multiple periods of time, where one period
accumulates something that rolls over to the next month.

Take for instance the following problem description:

.. code-block:: console

   A person has a capital of $300,000 and has 4 investment projects to choose from for the next
   three years.
   At the beginning of each year, money can be allocated to any of the 4 available projects.
   Investment returns that are released at the end of a year should be reinvested in the next year.

   ...

This description will generate all kinds of faulty models. We have not yet found a way of
making the LLM understand how it should be modelled.
