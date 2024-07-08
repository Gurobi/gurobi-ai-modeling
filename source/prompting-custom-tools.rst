Custom tools
============

Talk about Custom GPT and related here

Since the steps necessary for translating a problem description into an optimization model is well defined in :ref:`funnel` and
not necessarily changing we can utilize a Custom GPT that has these steps baked. Moreover, some common issues with the
current AI model can herein be addressed.

We have published a `Custom GPT <https://chatgpt.com/g/g-g69cy3XAp-optimization-modelling-assistant>`_ that incorporates this so users can focus on writing a problem description

Prompt Template
"""""""""""""""

We have seen a wide range of different problem description prompts that LLM's have successfully translated into
mathematical programs, even prompts that violate multiple of the  :ref:`tips and pitfalls <tips>` we mentioned earlier.

However, we want to stress the importance of taking a structured approach as this leads to a more predictable output as
the prompt will be more likely to contain all the necessary information and less likely to throw off the LLM because
of a confusing build up of the problem.

When using the above Custom GPT, we recommend utilizing the following prompt template and filling in the blanks:

.. code-block:: console

   Problem description:
   <describe the problem, making sure you mention all variables and constants>

   Objective: <Maximize/Minimize> <objective>
   Constraints:
   - <constraint name 1>: <describe constraint>
   - <constraint name 2>: <describe constraint>
   - <constraint name 3>: <describe constraint>
   - etc.

   Data:
   <data in csv format, including headers> or <upload your files and name the filename here>
