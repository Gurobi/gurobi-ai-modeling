.. _getting_started:

Getting Started
===============

Take a look at the following dietary problem.

.. code-block:: text

    I want to optimize my diet.

    Objective: I want to minimize the cost of food while upholding my dietary needs.

    Constraints:
    - I want to eat between 1800 and 2200 calories per day
    - At least 91 gram of protein
    - At most 65 gram of fat
    - At most 1779 mg of sodium


Next, let's look at some of the foods we can buy at our local grocery store:

.. code-block:: text

    +------------+--------+----------+-------------+---------+------------+
    | Food       | Price  | Calories | Protein (g) | Fat (g) | Sodium (mg)|
    +------------+--------+----------+-------------+---------+------------+
    | hamburger  | 2.49   | 410      | 24          | 26      | 730        |
    | chicken    | 2.89   | 420      | 32          | 10      | 1190       |
    | hot dog    | 1.50   | 560      | 20          | 32      | 1800       |
    | fries      | 1.89   | 380      | 4           | 19      | 270        |
    | macaroni   | 2.09   | 320      | 12          | 10      | 930        |
    | pizza      | 1.99   | 320      | 15          | 12      | 820        |
    | salad      | 2.49   | 320      | 31          | 12      | 1230       |
    | milk       | 0.89   | 100      | 8           | 2.5     | 125        |
    | ice cream  | 1.59   | 330      | 8           | 10      | 180        |
    +------------+--------+----------+-------------+---------+------------+


This is not an easy problem to solve by hand. Think about how you would try to satisfy the dietary needs. If you somehow
managed to find a combination of ingredients by hand that fit the nutritional goals, how would you know that you are
spending as little money as possible?

This combination of an objective with constraints is called an **optimization problem** and is something that can be
represented mathematically and subsequently solved by optimization tools. Unfortunately, even though we can all
understand the problem that was described earlier, many of us do not have the magical power to translate this into a
mathematical representation.

However, with the advent of Generative AI, the power of optimization might be put into the hands of many more people.

Using ChatGPT as a translator for mathematics
---------------------------------------------

We have crafted a `Custom GPT <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_ that helps with building and
solving an optimization model. Let's start by copying both the problem description and dataset we specified earlier and
paste it into the message box. [#f1]_

.. tip::

   Feel free to go ahead an try it yourself by heading to the `Custom GPT <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_
   and changing either the constraints or the nutritional data and see how it influences the model and its results!

.. container:: image-container

    .. image:: images/getting_started1.png
      :alt: Supplying the prompt
      :class: drop-shadow


The LLM now responds with the following template:

1. Problem Definition
^^^^^^^^^^^^^^^^^^^^^

First, the LLM translates the problem into a mathematical representation. We do this both for clarity as well
as increasing the chance of creating a successful model (more information on this in the :ref:`funnel` section).

.. container:: image-container

    .. image:: images/getting_started2.png
      :alt: Supplying the prompt
      :class: drop-shadow

2. Code generation and execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Then, the mathematical representation is used to generate ``gurobipy`` code in Python. The code is subsequently executed
on the remote server.

.. container:: image-container

    .. image:: images/getting_started3.png
      :alt: Supplying the prompt
      :class: drop-shadow

3. Result interpretation
^^^^^^^^^^^^^^^^^^^^^^^^

After the model has been solved, the results are explained.

.. container:: image-container

    .. image:: images/getting_started4.png
      :alt: Supplying the prompt
      :class: drop-shadow

At this stage, the user can add messages to the conversation for further steps. For instance:

- change the objective, constraints or data,
- ask for clarifications, advice or potential issues with the model,
- request the LLM to generate a graph with the results.

This was only a quick walkthrough of the project. In the following chapters we will dive into the details on how to
model optimization problems using LLMs. If you prefer to skip ahead and experiment with other example prompts, you can
also first head over to the :ref:`example_prompts` section. If you would like to write your own prompt from scratch, you
can start with our :ref:`prompt_template`.

.. [#f1] If ChatGPT takes you to a different page, make sure you are logged into ChatGPT prior to clicking the link.