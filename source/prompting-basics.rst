Basics
======

.. _persona:

Persona
-------
Instruct the LLM to act as a persona

.. _funnel:

Multi-step reasoning
----------------------
If one were to write a prompt that describes an optimization problem, the LLM can try to tackle it in a number of ways. The nature of LLM's is
such that the approach it takes will be different every time, with one being more successful than the other. Our goal should be
to achieve a prompt that is as effective and consistent as possible. To achieve this, we can nudge the LLM by including instructions for a successfully approach.

To get the most accurate and useful responses, it's helpful to break down complex tasks into smaller, logical steps. This process can be referred to as "multi-step reasoning" guiding the model to focus on one aspect of the task at a time. [`Fu et al., 2023  <https://openreview.net/forum?id=yf1icZHC-l9>`__, `Wang et al., 2024  <https://arxiv.org/abs/2305.04091>`__]
By breaking down a complex task into smaller steps, you can:

- **Reduce Ambiguity**: Smaller tasks are easier to understand and interpret correctly.
- **Increase Accuracy**: The model can focus on one specific aspect at a time, leading to more precise responses.
- **Improve Coherence**: Step-by-step instructions help maintain a logical flow, making the final output more coherent.

Now, if we turn back to the steps of turning a problem description into an optimization model, we find that it actually consists of the following steps:

.. grid:: 1
   :gutter: 2

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         Interpreting the question

   .. grid-item::
      .. raw:: html

         <div style="width: 50%; text-align: center; font-size: 24px;">&#8595;</div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         Generating the mathematical representation

   .. grid-item::
      .. raw:: html

         <div style="width: 50%; text-align: center; font-size: 24px;">&#8595;</div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         Generating the model

   .. grid-item::
      .. raw:: html

         <div style="width: 50%; text-align: center; font-size: 24px;">&#8595;</div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         Solving and result interpretation

Let's look at each of them in more detail:

Interpreting the question
^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about interpretation

Generating a mathematical representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about mathematical representation

Generating a model
^^^^^^^^^^^^^^^^^^
Talk about modeling

Solving and result interpretation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about solving and interpretation
