Custom GPTs
============

Since the steps necessary for translating a problem description into an optimization model are well defined in
:ref:`funnel`, we can leverage a feature that OpenAI's ChatGPT provides to have these steps baked-in: the Custom GPT.

We have published a Custom GPT called: `Gurobi AI Modeling Assistant <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_
which incorporates many of the reasoning steps and helps build, execute and interpret the results of the model
within ChatGPT so users can focus on writing an effective problem description.

See below for a walkthrough through the model building process using the Gurobi AI Modeling Assistant GPT:

.. carousel::
   :show_controls:
   :show_indicators:
   :show_dark:
   :data-bs-interval: false

   .. image:: images/customgpt1.png
      :alt: Gurobi AI Modeling Assistant

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

Leveraging the functionalities of a Custom GPT, we have also attached a ``gurobipy`` Python wheel, so ChatGPT
can model and optimize server-side [#]_.

With this, ChatGPT is sometimes able to spot mistakes it might make in a first draft of the code and fix them autonomously.

.. carousel::

   .. image:: images/customgpt2.png
      :alt: Custom GPT correcting itself

.. [#] Currently, the code execution environment of ChatGPT does not have access to the internet. This means it cannot download packages from PyPI. We can, however, upload wheels to the Custom GPT to give it access to ``gurobipy``.

.. _prompt_template:

Prompt Template
---------------

While it is possible to supply the Custom GPT with a wide range of problem-describing prompts, our advice is to write
your prompt following a template. We have devised the following prompt template that help guide users write a prompt
that contain the elements necessary for an optimization problem:

.. code-block:: console

   Problem description:
   As a <role> you are responsible for <job context>.
   <describe the problem on a high level, making sure you also introduce the context. Normally, 2-5 sentences is sufficient for this.>

   Objective: <Maximize/Minimize> <objective>
   Constraints:
   - <constraint name 1>: <describe constraint>
   - <constraint name 2>: <describe constraint>
   - <constraint name 3>: <describe constraint>
   - etc.

   Data:
   <data in csv format, including headers> or <upload your files and name the filename here>

As an added bonus, when one follows this template, users are more likely to think about these elements in a structured
way. Moreover, in the :ref:`example_prompts` section we will look at some example prompts we recommend trying out with
Gurobi AI Modeling Assistant. You will find that most of these prompts follow this template. After going through some of the
examples and subsequently using the same template, it should be more natural to follow our prompting recommended best
practices.

Gurobot
"""""""

Aside from Gurobi AI Modeling Assistant, Gurobi has put out another Custom GPT: `Gurobot <https://chatgpt.com/g/g-vPqYcfN7M-gurobot>`_.
Whereas `Gurobi AI Modeling Assistant <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_ is a very specific tool for
helping new users create models from a problem description, Gurobot is a general-purpose GPT
for asking Gurobi-related questions. We found that it performs better than using vanilla ChatGPT when
asking questions about, for instance, how to best add a specific constraint to your existing model.

.. note::
    Nevertheless, as with all LLMs, keep in mind that answers from Gurobot can be wrong or misleading. If in doubt, you
    may want to consult our human experts via our `Community Forum <https://support.gurobi.com/hc/en-us/community/topics>`_
    or the `Gurobi Help Center <https://support.gurobi.com/hc/en-us>`_.
