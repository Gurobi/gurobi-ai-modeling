Basics
======

Modelling in mathematical optimization is a discipline that requires multiple skills working in tandem:

1. **Domain knowledge** to translate a business problem into objectives and constraints
2. **Mathematics** to translate these into mathematical equations
3. **Modelling API usage** to translate the mathematical equations into code that represent them and retrieve the results

Most people working in the field of Operations Research that do this kind of work have had extensive training on order
to achieve these skills, and it's often not considered a skill you can pick up over the weekend. This sadly leaves
optimization out of the toolbox of many people that could benefit from it.

However, if you take a second look at the three skills listed above, all of them involve some kind of translation step.
With the advent of LLMs, we might be able to leverage tools like ChatGPT to assist us with some of the parts that
make optimization challenging for most of us mortals.

In the coming chapters we aim to explain through which steps LLMs can help with mathematical modelling and propose
a practical approach to bring it into the hands of users that have no prior knowledge of optimization.

Persona
-------
In the world of prompt engineering, it is generally understood that having the LLM assume a persona can help in guiding
the LLM into giving a relevant response with the depth and complexity that fits the specified persona. [`Nananukul et al., 2023  <https://arxiv.org/abs/2310.06174>`__]

In our case, we could prefix our system prompt with one of the following:

.. code-block:: console

   You are a seasoned expert in mathematical optimization and Python programming, with extensive experience using the gurobipy library for solving complex optimization problems.

or

.. code-block:: console

   Imagine you are a leading authority in the field of optimization algorithms and Python programming, with a particular focus on utilizing the pyomo library for modeling and solving optimization problems.

Of course, prompt engineering is not a one-size-fits-all solution and different LLMs respond differently to the same
prompt, and behavior for the same LLM is likely to change over time as the model is updated by its vendor, so what
exactly constitutes a "good" persona definition is subject to change.

.. _funnel:

Multi-step reasoning
--------------------
Generally speaking, supplying the same prompt to an LLM multiple times, will yield you a different output every time
(there are hyperparameters like 'temperature' that influence this, but this is unleveraged by most users). This means
that trying to do mathematical modelling through such tools yields very inconsistent results.

For instance, in your first conversation you might get an output that is well-structured, shows that the LLM understood
you question, generated a valid model and even helped you interpret the results. You are happy, and later you want to
try again with a slightly different prompt. However, this time, the LLM only generates the code without explaining to
you how it interpreted your prompt. Moreover, even though it generated a model that is able to solve, it did not give
you the code to extract and interpret the solution for you, leaving you to figure that out for yourself.

A solution for this would be to tell the LLM *how* to respond. The following example shows a prompt snippet where we
instruct the LLM how to structure its respond for a more reliable output:

.. code-block:: console

   Your response will follow the template:

   {If the user provides any data files, read them and make sure you understand the complete context before moving on}
   ## 🔢 Problem definition
   {Convert the problem description into a mathematical model. Use proper mathematical notations}
   ## 🐍 Build and solve model
   {Create and solve the model using Code Interpreter. Model non-divisible items as integer variables.}
   ## 👩‍🏫 Results
   {Display solution, objective values and decision variables. Note any unaddressed aspects.}

If you think back to the first paragraph of this chapter, you might see a similarity between both structures. This
is not a coincidence, and at this point we want to introduce a concept in prompt engineering: *Multi-step Reasoning*
or *Chain-of-Thought*. This is the concept of breaking down complex tasks into smaller, logical steps. [`Fu et al., 2023  <https://openreview.net/forum?id=yf1icZHC-l9>`__, `Wang et al., 2024  <https://arxiv.org/abs/2305.04091>`__]

An LLM generates its response word-by-word, taking both the prompt and the generated response up until that
point into consideration. This means that we can help the LLM by making it generate text that it can itself then
later use to eventually create a response that is more complex that it would have otherwise been able to.

To break it down, we aim to achieve the following steps:


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

Let's look at each of the steps in more detail:

Interpreting the question
^^^^^^^^^^^^^^^^^^^^^^^^^
The LLM will obviously read your prompt in full. However, you might want to supply containing data or information
with your prompt as well. LLMs like ChatGPT will automatically read and interpret some data types (like .csv), but
not all. Often these data files contain information that is important for formulating the mathematical model. For
instance, some columns might be binary while others are floats, which could influence how the model should be
constructed. By intructing the LLM to read in any attached files, you increase the chance of it being able to interpret your
problem correctly and getting a valid model at the end.

Alternatively, there might be other concepts that you want the LLM to think about when interpreting your question. For
instance, your problem description might include the usage of AWS EC2 instances. In this case the LLM could be
instructed to fetch the latest instance data to make sure it has the most up-to-date information about which
instances are available and their characteristics.

Generating a mathematical representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function of this step is two-fold. The first being that it gives the user assurance that the LLM has understood
the problem correctly. It will restructure your question into a collection of objectives and constraints, which allows
the user to investigate whether the problem was understood, whether the right assumptions were made and, last but not
least, whether any assumptions the user might have made are not represented in the model. Especially the last one is
a pitfall to keep in mind: we might think that some concepts don't need to be mentioned, but how an LLM choses
to interpret your words can often be unexpected.

The second function of this step is to fulfill the aforementioned concept of *Multi-step Reasoning*. To be most
effective we currently recommend to make the LLM generate the model in mathematical notation. Even if the user
might not be able to understand it, we feel that it leads to a better model generation later on.

Generating a model
^^^^^^^^^^^^^^^^^^
Talk about modeling

Solving and result interpretation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about solving and interpretation
