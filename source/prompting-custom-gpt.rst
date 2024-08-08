Custom GPTs
============

Since the steps necessary for translating a problem description into an optimization model is well defined in :ref:`funnel` and
not necessarily changing we can utilize a Custom GPT that has these steps baked. Moreover, some common issues with the
current LLM can herein be addressed.


We have published a Custom GPT called: `Gurobi Model Builder <https://chatgpt.com/g/g-g69cy3XAp-gurobi-model-builder>`_.
This Custom GPT incorporates some of the reasoning steps and helps build, execute and interpret the results of the model
within ChatGPT so users can focus on writing an effective problem description.

.. thumbnail:: images/customgpt1.png
   :align: center

   Gurobi Model Builder

For a walkthrough, see the following set of images:

.. subfigure:: ABC|DEF|GHI
   :layout-sm: A|B|C|D|E|F|G|H|I
   :subcaptions: above
   :name: walkthrough
   :gap: 0px
   :class-grid: outline

   .. thumbnail:: images/walkthrough1.png
      :width: 100%
      :group: group1

      Input prompt

   .. thumbnail:: images/walkthrough2.png
      :width: 100%
      :group: group1

      First output showing the model's mathematical formulation

   .. thumbnail:: images/walkthrough3.png
      :width: 100%
      :group: group1

      The rest of the mathematical formulation

   .. thumbnail:: images/walkthrough4.png
      :width: 100%
      :group: group1

      Gurobipy code representing the model

   .. thumbnail:: images/walkthrough5.png
      :width: 100%
      :group: group1

      The rest of the gurobipy code

   .. thumbnail:: images/walkthrough6.png
      :width: 100%
      :group: group1

      Currently, we need to manually trigger ChatGPT to run the code on their infrastructure

   .. thumbnail:: images/walkthrough7.png
      :width: 100%
      :group: group1

      Showing the code again, but now in a Code Analysis block that can run code (indicated by Analyzed in the top-left corner)

   .. thumbnail:: images/walkthrough8.png
      :width: 100%
      :group: group1

      Gurobipy logs showing the solve progress

   .. thumbnail:: images/walkthrough9.png
      :width: 100%
      :group: group1

      Finally, ChatGPT helps interpret the results

Advantages
""""""""""

Moreover, having ChatGPT build and run the model inside the platform, it is sometimes able to spot and recover from
mistakes it might initially make.

.. thumbnail:: images/customgpt2.png
   :align: center

   Custom GPT correcting itself

Prompt Template
"""""""""""""""

In the :ref:`example_prompts` section we will look at some example prompts that you can use with Gurobi Model Builder.
For the most part, the prompts will follow the following prompt template:

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

It is not strictly necessary to utilize this template. However, we do recommend taking a structured approach as it likely
leads to a more reliable output as it increases the likelihood of your prompt to contain all the necessary information
and less likely to throw off the LLM because of a confusing structuring of the problem description.

Gurobot
"""""""

We have also put out a second Custom GPT: `Gurobot <https://chatgpt.com/g/g-vPqYcfN7M-gurobot>`_.
Whereas `Gurobi Model Builder <https://chatgpt.com/g/g-g69cy3XAp-gurobi-model-builder>`_ is a very specific tool for
helping new users create models from a problem description, Gurobot is a general-purpose GPT
for asking Gurobi-related questions. We found that it performs better than using vanilla ChatGPT when
asking questions about, for instance, how to best add a specific constraint to your existing model.