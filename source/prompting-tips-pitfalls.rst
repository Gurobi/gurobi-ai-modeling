.. _tips_and_pitfalls:

Tips and pitfalls
==================

During the course of this project and formulating the :ref:`example_prompts` section, we have come across common tips
and pitfalls relating to prompting and handling LLMs in general. In the current section we will share our findings that
relate to modeling optimization problems using LLMs and help set you up for prompting success.

Write problems as unambiguous as possible
-----------------------------------------
As human beings, we often make a similar mistake in our casual and business interactions: assuming the other party holds the same definition of the
words we use. Such a semantic conflict can cause confusion when you send somebody on an errand and the person comes back
with something else than you had expected. Humans often have procedures for this by asking clarifying questions:
`what exactly do you mean by ...?`. Unfortunately, the current generation of LLMs does not seem to express the degree
of confusion under which they are generating a response, leading it to just make assumptions about what you mean.

Currently the only way of dealing with this is by making sure your prompt is as unambiguous as possible.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Minimize energy consumption.

   .. tab:: Good

      .. code-block:: text

         Minimize the total energy consumption of all production facilities, defined as the sum of electricity, fuel, and water usage.

Or to bring it into the domain of Software Engineers:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to deploy 5 applications on AWS using either EC2 and/or Fargate, but minimizing costs.
         Each application has specific CPU and RAM requirements, and you need to decide whether to deploy them on AWS EC2 instances or Fargate.

         Objective: Minimize total deployment cost

   .. tab:: Good

      .. code-block:: text

         I want to deploy 5 applications on AWS using either EC2 and/or Fargate, but minimizing costs.

         Objective: Minimize total monthly deployment costs.

         Constraints:
         - There should be 1 of every application.
         For EC2 instances:
           - One EC2 instance can run multiple Apps
           - The combined vCPU and RAM usage cannot exceed a single EC2 instance's capability
           - You can instantiate multiple EC2 instances of the same type
         For Fargate instances:
           - One Fargate instance can only run one App
           - The vCPU and RAM usage cannot exceed the Fargate instance capability
           - You can instantiate multiple Fargate instances of the same type


Unexpected prompts can lead to unexpected behavior
--------------------------------------------------
You might remember that an LLM is just statistically reciting tokens it has seen before. If your prompt is doing
something that the LLM deems `unexpected`, it might cause it either:

1. blindly follow your instructions, or
2. exert behavior that looks like it assumes you made a mistake and just selectively augments part of your prompt.

To illustrate this, in one of our Examples, there used to be an equation for calculating total shipping costs on an
E-commerce platform:

.. code-block:: console

   - Total Shipping costs: SC = Base Shipping Cost+(2×Size (kg))+(1.5×Weight (kg))

It states the total shipping costs depends on a base cost and weight of the item category. We actually forgot to mention
that the number of shipped products should also be included. We found that the LLM ended up being confused by this and
exerting non-deterministic behavior, sometimes adding the number of products, sometimes leaving it as is, and sometimes
coming up with something else entirely. From its behavior, it seemed that it was somehow `expecting` the number of
items shipped to be part of the equation.

This is where your knowledge of the problem comes in. If the shipping cost indeed should depend on the number of items
shipped, it should be reflected in the equation:

.. code-block:: console

   - Shipping costs: SC = Base Shipping Cost + ((2×Size (kg))+(1.5×Weight (kg)) * units sold)

If it is somehow not dependent on the number of items shipped, we can improve the prompt a little bit by stating this
fact explicitly:

.. code-block:: console

   - Shipping costs: SC = Base Shipping Cost+(2×Size (kg))+(1.5×Weight (kg)). The total shipping cost is independent on the number of items shipped.

Should variables be considered divisible or not?
------------------------------------------------
In many cases, the LLM will be able to deduce whether the variables involved in the problem should be divisible
or not. For instance, cars are very likely to be non-divisible (nobody wants ``0.54`` of a car), while kilograms are likely considered divisible.

However, if this is not unambiguously clear from the item itself, it will be helpful to mention how it
should be considered.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to optimize my diet.

         Objective: I want to minimize the cost of food while upholding my dietary needs.

         Constraints:
         - I want to eat between 1800 and 2200 calories per day
         - At least 91 gram of protein
         - At most 65 gram of fat
         - At most 1779 mg of sodium

         ...


   .. tab:: Good

      .. code-block:: text

         I want to optimize my diet.

         Objective: I want to minimize the cost of food while upholding my dietary needs.

         Constraints:
         - I want to eat between 1800 and 2200 calories per day
         - At least 91 gram of protein
         - At most 65 gram of fat
         - At most 1779 mg of sodium
         - Portions are non-divisible

         ...

Avoid unnecessary words or statements
-------------------------------------
If you, again, think about how an LLM works, it's all about predicting the next token based on what was given before.
The implication of this is that one should avoid adding unnecessary words lest not to confuse the LLM. Let's take an
example of a bad and good pattern. The following shows a description of the objective of a data flow problem where
data can be sent via any route through the nodes :math:`\{0,1,2,3,4,5\}`:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Imagine we're managing a telecommunications network that spans 6 key points, from a primary data center (Point 0) to a major user hub (Point 5).

         ...

         The objective is to find out the maximum amount of data that can be transferred from Point 0 (Data Center) to Point 5 (User Hub) per second.


   .. tab:: Good

      .. code-block:: text

         Imagine we're managing a telecommunications network that spans 6 key points, from a primary data center (Point 0) to a major user hub (Point 5).

         ...

         The objective is to find out the maximum amount of data that can be transferred to Point 5 (User Hub) per second.

For a human, the objective should be clear for either version: maximize the flow into Point 5. A machine might have more
difficulty with it and consider multiple options:

1. Maximize for Point 5 inflow?
2. Maximize for Point 0 outflow?
3. Maximize the direct flows from 0 to 5 and disregard the indirect flows into 5?

Even though option 2 and 3 might seem intuitively wrong to the human eye (and an LLM should be able to be able to
interpret it that way), it is exactly these kind of small sources of confusion that compound together with other
ambiguities in the prompt that lead to an output that is overall less precise.

A very simple solution for this is proposed in the Good example: `keep things as simple as possible`.

Supply all necessary (dummy) data
---------------------------------
As alluded to in the previous paragraphs, the current generation of LLMs will not tell the degree of uncertainty it
is generating the response under. Because of this, if you forget to supply any data, be it a single column or the whole
data set, it will not prompt you or express confusion.

It might either adapt its interpretation of the problem and leave out some important aspect that requires that data, or
it might generate some dummy data on its own accord without asking you.

Obviously, one should exercise restraint about supplying proprietary or private data to commercial LLMs. We therefore suggest
creating a dummy or anonymized dataset.

Technical Issues
----------------
Working with LLMs is currently fraught with inconsistent technical behavior. For instance, ChatGPT
has a number of very cool integrations that we can make use of, however, sometimes they experience intermittent issues
which cause them to stop working for a period of time.

Often the best remedy is to try again, or in some cases, just come back later. Here are some of the issues that we
occasionally encountered:

The LLM cannot install the wheel or cannot read attached data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the LLM prompts you to install a wheel or attach a data file which you have already attached, it is likely
an intermittent system issue. The LLM could also tell you that it is not able find the required file:

.. code-block:: console

   I cannot find the .whl feel you are trying to install


In many cases this can be solved by starting a new chat window, or, as stated previously, wait for the system issue to be
resolved.

LLM is generating code but not executing it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you instruct the LLM to execute code, it should be able to comply and generate code into an environment
that can execute it. However, it can happen that code is generated without it being executed.

This can mean two things:

1. The LLM thinks it can get away with just generating code and not executing it, assuming you will execute the code on your own machine. In many cases, the solution to this is to nudge the LLM to: ``execute the code``.
2. The LLM can also be experiencing technical difficulties and cannot access its code execution environment. In this case telling it to ``execute the code`` might result in a response like:

   .. code-block:: console

      It seems that I am currently unable to execute the code directly

   Even worse, it can also happen that it is not able to do this introspection and it will ignore your request and blindly regenerates the code again with, again, skipping the execution.

Both behaviors listed in 2. are often solved by either starting a new conversation and trying again, or waiting for a
while until the issues are resolved.

Advanced Gurobipy API's
-----------------------
Most of the data utilized for training the current generating of LLMs contain data using earlier versions of ``gurobipy``
API's. This is generally not a problem since the ``gurobipy`` API is quite stable (this is by design). However, it does
mean that the LLM is less prone to using the newest advanced API's which allow for building models with more complex
constraints like quadratic or nonlinear constraints. For simple models however, these advanced API's should
not be needed.

Too much gurobipy output
------------------------
In some cases you might need to solve a large number of models. For instance, when solving a model multiple times while
varying the value of a constant (eg. in a strategy called a `Pareto Front <https://en.wikipedia.org/wiki/Pareto_front>`__
or `efficient frontier`). We show this in the :ref:`portfolio <portfolio>` example.

This can lead to a large amount of logging output from Gurobi. Especially if you work with a platform like ChatGPT,
which can run the code within Code Analysis blocks, this will consume a large number of tokens and could lead to
adverse effects. For such cases we recommend instructing the LLM to suppress logging output (which should add
``model.setParam("OutputFlag", 0)`` to the resulting code).

Other modeling Pitfalls
-----------------------
The one thing to always keep in mind is that almost never will the LLM express any doubts about interpreting your question. It will make assumptions and when generating an answer will try to sound authoritative.
This is why you have to make extra sure that you don't fall for any of the pitfalls that lead to bad results, since it might not be obvious where the error lies that tripped up the model.

It is all about removing as many impediments for the LLM as possible, so it can focus on the problem at hand.

Below you can find a few small ways in which you can trip up the LLM:

Typos
^^^^^
Confusing a ``0`` (zero) with an ``O`` (capital o).

Mixing data types
^^^^^^^^^^^^^^^^^
Mixing both integers and floats in a column in your dataset is likely to be successfully parsed and handled by the LLM, but given this section's preamble, it's advised to stay consistent.

Too much inline data
^^^^^^^^^^^^^^^^^^^^
Our experimentation found that LLMs can work with a surprisingly wide variety of formatted data, csv, markdown, LaTeX,
and others it can often read with no problem. Where it does start to become problematic is too much inline data as they
represent tokens that it will need to be taken into account into the full context.

Our recommendation is that if you have more than 10 lines of data, it should be stored into a data file that is uploaded
with the prompt.

Data preprocessing
^^^^^^^^^^^^^^^^^^
In many cases you can supply raw data to the LLM and instruct it how to preprocess it and extract meaning from it.
However, any of these steps add complexity to the overall problem, it is therefore advised to do the preprocessing
of the data and extracting of features so that the LLM focus on the optimization problem in isolation.