Basics
======

Modeling in mathematical optimization is a discipline that requires multiple skills working in unison:

1. **Domain knowledge** to translate a business problem into objectives and constraints
2. **Mathematics** to translate these objectives and constraints into mathematical equations
3. **Modeling API usage** to translate the mathematical equations into code that represent them and retrieve the results

Most people working in the field of Operations Research that do this kind of work have had extensive academic and
professional training in order to achieve these skills, and these are generally not considered skills you can pick up
over the weekend. This sadly leaves optimization out of the toolbox of many people that could benefit from it.

However, if you take a second look at the three skills listed above, all of them involve some kind of manner of
translation. With the advent of LLMs, we might be able to leverage tools like ChatGPT to assist us with some of the
parts that make optimization challenging for most of us mere mortals.

In the coming chapters we aim to explain through which steps LLMs can help with mathematical modeling and propose
a practical approach to bring it into the hands of users that have no prior knowledge of optimization. Let us first
start with some basic LLM concepts.

Prompt engineering
------------------
In the world of prompt engineering, it is generally understood that having the LLM assume a persona can help in guiding
the LLM into giving a relevant response with the depth and complexity that fits the specified persona [#]_. [`Nananukul et al., 2023  <https://arxiv.org/abs/2310.06174>`__]

In our case, we could prefix our system prompt with one of the following:

.. code-block:: console

   You are a seasoned expert in mathematical optimization and Python programming, with extensive experience using the gurobipy library for solving complex optimization problems.

or

.. code-block:: console

   Imagine you are a leading authority in the field of optimization algorithms and Python programming, with a particular focus on utilizing the pyomo library for modeling and solving optimization problems.

Of course, prompt engineering is not a one-size-fits-all solution and different LLMs respond differently to the same
prompt, and behavior for the same LLM is likely to change over time as the model is updated by its vendor, so what
exactly constitutes a `good` persona definition is subject to change.

.. [#] We also recommend reading `this  <https://arxiv.org/abs/2406.06608>`__ excellent meta-analysis paper on prompting techniques!

.. _funnel:

Answer engineering
------------------
Generally speaking, supplying the same prompt to an LLM multiple times, will yield you a different output every time
(there are hyperparameters like `temperature` that influence this, but this is not leveraged by most casual users). Such
inconsistent output poses a challenge we would need to address:

For instance, in your first conversation you might get an output that is well-structured, shows that the LLM understood
you question, generated a valid model and even helped you interpret the results. You are happy, and later you want to
try again with a slightly different prompt. However, this time, the LLM only generates the code without explaining to
you how it interpreted your prompt. Moreover, even though it generated a model that can be solved, it did not give
you the code to extract and interpret the solution for you, leaving you to figure that out for yourself.

A solution for this would be to, in addition to your initial prompt, also tell the LLM *how* to respond. The following
example shows a prompt snippet where we instruct the LLM how to structure its response for a more reliable output:

.. code-block:: console

   Your response will follow the template:

   {If the user provides any data files, read them and make sure you understand the complete context before moving on}
   ## 🔢 Problem definition
   {Convert the problem description into a mathematical model. Use proper mathematical notations}
   ## 🐍 Build and solve model
   {Create and solve the model using Code Interpreter. Model non-divisible items as integer variables.}
   ## 👩‍🏫 Results
   {Display solution, objective values and decision variables. Note any unaddressed aspects.}

However, there is another reason to take this approach.
If you think back to the first paragraph of this chapter explaining the skills working in unison necessary for
modeling, you might have noticed some similarities. This is not a coincidence, and at this point we want to introduce
a concept in prompt engineering: *Chain-of-Thought (CoT)*. This is the concept of breaking down
complex tasks into smaller, logical steps. [`Fu et al., 2023  <https://openreview.net/forum?id=yf1icZHC-l9>`__, `Wang et al., 2024  <https://arxiv.org/abs/2305.04091>`__]

An LLM generates its response word-by-word, taking both the prompt and the generated response up until that
point into consideration. This means that we can nudge the LLM into the right direction by making it generate text that
it will later use, eventually creating a response that is more complex that it would have otherwise been able to provide
(it is assumed that the recently released ``o1`` model by OpenAI uses this approach).

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

         Interpreting the results

Let's look at each of the steps in more detail:

Interpreting the question
^^^^^^^^^^^^^^^^^^^^^^^^^
The LLM will obviously read your prompt in full. However, you might want to supply containing data or information
with your prompt as well. Some LLMs like ChatGPT will automatically read and interpret some attached data files if they
are in a specific file format (like .csv), but often this does not apply to all file formats. Often these data files contain
information that is important for formulating the mathematical model. For instance, some columns might be binary while
others are floating point numbers, which could influence how the model should be constructed. By instructing the LLM to read in any
attached files, you increase the chance of it being able to interpret your problem correctly and getting a valid model
at the end.

Alternatively, there might be other concepts that you want the LLM to think about when interpreting your question. For
instance, your problem description might include the usage of AWS EC2 instances. Working with such concepts, the LLM
could be instructed to fetch the latest instance data to make sure it has the most up-to-date information about which
instances are available and their characteristics.

Generating a mathematical representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function of this step is two-fold:

1. The first being that it gives the user assurance that the LLM has understood
   the problem correctly. It will restructure your question into a collection of objectives and constraints, which allows
   the user to investigate whether the problem was understood, whether the right assumptions were made and, last but not
   least, whether any assumptions the user might have made are not represented in the model. Especially the last one is
   a pitfall to keep in mind: we might think that some concepts are obvious and don't need to be specifically defined,
   but an LLM can often surprise us with how it chooses to interpret your words.

2. The second function of this step is to fulfill the aforementioned concept of *Chain-of-Thought*. To be most
   effective we currently recommend to make the LLM generate the model in mathematical notation. Even if the user
   might not be able to understand it, we feel that it leads to a better model generation later on.

Generating a model
^^^^^^^^^^^^^^^^^^
In this step we can do a few things:

1. Instruct the LLM to not only generate the code, but also run it server-side. Doing this has tremendous benefit as
   the LLM can immediatly get feedback from its own work:

   - if the code has errors it can attempt to fix it, or
   - if the model is infeasible it can do a sanity check to make sure the model was set up correctly.

2. You can also steer the LLM slightly on how to utilize the modeling API:

   - In the aforementioned template example we instructed the LLM to set up variables representing non-divisable items
     (like a car) as an integer variable type rather than a floating point type.
   - If the LLM is prone to using an outdated API of the modeling package (because it was trained on old information)
     you might be able to instruct it to utilize a newer API. We do note that we have had inconsistent results with this
     and currently recommend letting the LLM model utilize the API it prefers (and is apparently most comfortable with),
     even if it means not following current best practices.

Interpreting the results
^^^^^^^^^^^^^^^^^^^^^^^^
If you have never used optimization, you might find that the challenge does not end with successfully solving a model
to optimality. Extracting the values you are interested in for your business problem and interpreting them also requires
some amount of training. Luckily, this is a task that the LLM should also be able to handle. This is also why running
the model server-side is so important. It knows how to query which data points and helps you paint a picture on what
it all means.
