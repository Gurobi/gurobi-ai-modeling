Custom GPTs
============

Since the steps necessary for translating a problem description into an optimization model is well defined in :ref:`funnel` and
not necessarily changing we can utilize a Custom GPT that has these steps baked. Moreover, some common issues with the
current LLM can herein be addressed.


We have published a Custom GPT called: `Gurobi Model Builder <https://chatgpt.com/g/g-g69cy3XAp-gurobi-model-builder>`_.
This Custom GPT incorporates some of the reasoning steps and helps build, execute and interpret the results of the model
within ChatGPT so users can focus on writing an effective problem description.

See below for a walkthrough through the model building process using the Gurobi Model Builder GPT:

.. carousel::
   :show_controls:
   :show_indicators:
   :show_dark:
   :data-bs-interval: false

   .. image:: images/customgpt1.png
      :alt: Gurobi Model Builder

   .. image:: images/walkthrough1.png
      :alt: Input prompt

   .. image:: images/walkthrough2.png
      :alt: First output showing the model's mathematical formulation

   .. image:: images/walkthrough3.png
      :alt: The rest of the mathematical formulation

   .. image:: images/walkthrough4.png
      :alt: Gurobipy code representing the model

   .. image:: images/walkthrough5.png
      :alt: The rest of the gurobipy code

   .. image:: images/walkthrough6.png
      :alt: Currently, we need to manually trigger ChatGPT to run the code on their infrastructure

   .. image:: images/walkthrough7.png
      :alt: Showing the code again, but now in a Code Analysis block that can run code (indicated by Analyzed in the top-left corner)

   .. image:: images/walkthrough8.png
      :alt: Gurobipy logs showing the solve progress

   .. image:: images/walkthrough9.png
      :alt: Finally, ChatGPT helps interpret the results

Advantages
""""""""""

Additionally, having ChatGPT build and run the model inside the platform, it is sometimes able to spot and recover from
mistakes it might initially make.


.. carousel::

   .. image:: images/customgpt2.png
      :alt: Custom GPT correcting itself

Prompt Template
"""""""""""""""

While it is possible to supply the custom GPT with a wide range of problem-describing prompts, our advice is to write
your prompt following a template. We have devised the following prompt template that help guide users write a prompt
that contain the elements necessary for an optimization problem:

.. code-block:: console

   Problem description:
   <describe the problem on a high level, making sure you also introduce the context. Normally, 3-5 sentences is sufficient for this.>

   Objective: <Maximize/Minimize> <objective>
   Constraints:
   - <constraint name 1>: <describe constraint>
   - <constraint name 2>: <describe constraint>
   - <constraint name 3>: <describe constraint>
   - etc.

   Data:
   <data in csv format, including headers> or <upload your files and name the filename here>

When following this template you are more likely to think about these elements in a structured way. Moreover, in the
:ref:`example_prompts` section we will look at some example prompts we recommend trying out with Gurobi Model Builder.
You will find that most of these prompt follow this template. After going through some of the examples and subsequently
using the same template, it should be more natural to follow our prompting recommended best practices.

Gurobot
"""""""

Additionally, Gurobi has put out another Custom GPT: `Gurobot <https://chatgpt.com/g/g-vPqYcfN7M-gurobot>`_.
Whereas `Gurobi Model Builder <https://chatgpt.com/g/g-g69cy3XAp-gurobi-model-builder>`_ is a very specific tool for
helping new users create models from a problem description, Gurobot is a general-purpose GPT
for asking Gurobi-related questions. We found that it performs better than using vanilla ChatGPT when
asking questions about, for instance, how to best add a specific constraint to your existing model.