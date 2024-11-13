Writing your first prompt
=========================

At this point, you might still wonder how to get started on writing an prompt. In :doc:`intro-getting-started`, we
were presented with a problem description and constraints. In :doc:`intro-usecases` some possible applications were
mentioned.

But how can we now find use cases in our daily life? It is very likely that there are multiple opportunities for
optimization in both your daily professional and personal encounters [#f1]_. However, to identify those it requires
looking at challenges through the lens of optimization. If you are new to optimization, this likely does not come naturally (yet).

To put it clearly, taking the route of utilizing an LLM to build and solve an optimization model you would need to
traverse the following steps:

.. grid:: 1
   :gutter: 2

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         1\. Recognize a situation as an optimization problem

   .. grid-item::
      .. raw:: html

       <div style="width: 50%; text-align: center;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="M4.97 13.22a.75.75 0 0 1 1.06 0L11 18.19V3.75a.75.75 0 0 1 1.5 0v14.44l4.97-4.97a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734l-6.25 6.25a.75.75 0 0 1-1.06 0l-6.25-6.25a.75.75 0 0 1 0-1.06Z"></path></svg>
       </div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         2\. Identify the elements in the problem (objective, constraints & data)

   .. grid-item::
      .. raw:: html

       <div style="width: 50%; text-align: center;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="M4.97 13.22a.75.75 0 0 1 1.06 0L11 18.19V3.75a.75.75 0 0 1 1.5 0v14.44l4.97-4.97a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734l-6.25 6.25a.75.75 0 0 1-1.06 0l-6.25-6.25a.75.75 0 0 1 0-1.06Z"></path></svg>
       </div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         3\. Write down these elements into a well-written and unambiguous LLM prompt

   .. grid-item::
      .. raw:: html

       <div style="width: 50%; text-align: center;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="M4.97 13.22a.75.75 0 0 1 1.06 0L11 18.19V3.75a.75.75 0 0 1 1.5 0v14.44l4.97-4.97a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734l-6.25 6.25a.75.75 0 0 1-1.06 0l-6.25-6.25a.75.75 0 0 1 0-1.06Z"></path></svg>
       </div>

   .. grid-item::
      .. card::
         :shadow: md
         :text-align: center
         :width: 50%

         4\. Generate and solve the model and interpret the results

You could say that in the :doc:`intro-getting-started` chapter we only demonstrated Step 4. Steps 1-3 all
require getting acquainted with the elements of optimization and learning to recognize these problems in the wild.

Here, again, we found that ChatGPT can be of help. To support Steps 1-3 we have devised another Custom GPT called
`Gurobi AI Modeling Prompt Engineer <https://chatgpt.com/g/g-JK2EuyVOt-gurobi-ai-modeling-prompt-engineer>`_. This GPT
should act as an optimization expert to assist with Steps 1 and 2, and once you collaboratively have come to a defined
problem, the GPT should propose a prompt (Step 3) that you can then hand over to `Gurobi AI Modeling Assistant <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_
to generate and solve the model.

.. grid:: 5
    :gutter: 1

    .. grid-item-card::

        .. raw:: html

            <a href="https://chatgpt.com/g/g-JK2EuyVOt-gurobi-ai-modeling-prompt-engineer" target="_blank">
                <img src="_static/_images/gurobi_logo_text3.png" alt="Gurobi AI Modeling Prompt Engineer" />
            </a>

        .. raw:: html

            </a><span style="font-size: 0.85em;">Gurobi AI Modeling Prompt Engineer</span>

    .. grid-item::
       .. raw:: html

          <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1;">
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48">
                <path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0Z"></path>
             </svg>
             <div style="margin-top: 4px; font-size: 0.85em; text-align: center; line-height: 1.2;">
                Explore, identify and create the prompt
             </div>
          </div>

    .. grid-item-card::

        .. raw:: html

            <a href="https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant" target="_blank">
                <img src="_static/_images/gurobi_logo_gear3.png" alt="Gurobi AI Modeling Assistant" />
            </a>

        .. raw:: html

            <span style="font-size: 0.85em;">Gurobi AI Modeling Assistant</span>

    .. grid-item::
       .. raw:: html

          <div style="width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1;">
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48">
                <path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0Z"></path>
             </svg>
             <div style="margin-top: 4px; font-size: 0.85em; text-align: center; line-height: 1.2;">
                Generate the model
             </div>
          </div>

    .. grid-item-card::

        .. image:: images/gears.png
            :alt: Optimization Model

        .. raw:: html

            <span style="font-size: 0.85em;">Optimization Model</span>

For instance, we can start with the following prompt:

.. code-block:: text

    I am a CFO and need to decide how to divide bonuses across the organization. What are the elements that I can take into consideration for optimizing this?

.. container:: image-container

    .. image:: images/prompting1.png
      :alt: Supplying the prompt
      :class: drop-shadow

The GPT will likely give some ideas which factors might be of interest to take into account:

.. container:: image-container

    .. image:: images/prompting2.png
      :alt: First response
      :class: drop-shadow

To answer these questions, we can say something like:

.. code-block:: text

    I have a total of 20% of revenue as bonus to award. There are some team limits defined as percentages of the total bonus pool.
    I want to use team performance metrics.
    Higher level people should get more bonus.
    Tenure is a variable that should get taken into account.
    I also want to give some teams a little bit more since they worked a lot of overtime this year.

.. container:: image-container

    .. image:: images/prompting3.png
      :alt: Answering questions
      :class: drop-shadow

At this point, the GPT will either:

1. ask follow-up questions, or
2. decide it has enough information to come up with a prompt for Gurobi AI Modeling Assistant.

.. important::

    If the GPT has decided on option 2, you should take a moment and reflect whether the prompt does exactly what you want and is
    as unambiguous as possible. Poorly written or incomplete prompts will still lead to incomplete or bad models.

In the second case, the output should follow a prompt template from a :ref:`future chapter <prompt_template>`:

.. container:: image-container

    .. image:: images/prompting4.png
      :alt: Answering questions
      :class: drop-shadow

.. container:: image-container

    .. image:: images/prompting5.png
      :alt: Answering questions
      :class: drop-shadow

If you are happy with this prompt. The next step will be to collect the necessary data to supply to the prompt.
To get an idea of what this data could look like, our :doc:`prompting-examples` section has many examples that
utilizes external data, but you could also use inline data as in :doc:`intro-getting-started`. In the future, we should
probably write a section about which data types are suitable in this context.

At this point, it is highly recommended to take a look at some of the :doc:`prompting-examples` to get inspiration on
what an effective an unambiguous prompt looks like.


.. [#f1] Whether all daily problems are suitable to be formalized into a
    optimization problem is of course another question...