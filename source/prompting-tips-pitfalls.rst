Tips and pitfalls
==================

.. _tips:

Tips
-------

Unambiguous problem statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about unambiguous problem statement

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Maximize the coverage of different test environments (EnvA, EnvB, EnvC).
         Prioritize machines that have not been tested on recently (considering the latest test_timestamp).
         Prioritize machines on which the test did not pass last time

   .. tab:: Good

      .. code-block:: text

         Pears are green.


Should variables be considered divisible or not?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In many cases, the LLM will be able to deduce whether the variables involved in the problem should be divisible
or not. For instance, cars are very likely to be non-divisible, while kilograms are likely considered divisible.

However, if this is not unambiguously clear from the item itself, it will be helpful to mention how it
should be considered.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to minimize the cost of food while upholding my dietary needs.

         The following food I want to choose between is as follows, it is a comma-delimited table with the following columns: food, price, calories, protein, fat, sodium:
         salad,2.49,320,31,12,1230

         ...


   .. tab:: Good

      .. code-block:: text

         I want to minimize the cost of food while upholding my dietary needs.
         Portions are non-divisible.

         The following food I want to choose between is as follows, it is a comma-delimited table with the following columns: food, price, calories, protein, fat, sodium:
         salad,2.49,320,31,12,1230

         ...

Avoid unnecessary words or statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you think about how an LLM works, it's all about predicting the next token based on what was given before. The
implication of this is that one should avoid adding unnecessary words lest not to confuse the LLM. Let's take an
example of a bad and good pattern. The following shows a description of the objective of a data flow problem where
data can be sent via any route through the nodes :math:`\{0,1,2,3,4,5\}`:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         ...

         The objective is to find out the maximum amount of data that can be
         transferred from Point 0 (Data Center) to Point 5 (User Hub) per second.


   .. tab:: Good

      .. code-block:: text

         ...

         The objective is to find out the maximum amount of data that can be
         transferred to Point 5 (User Hub) per second.

For a human, the objective should be clear for either version: maximize the flow into Point 5. A machine might have more
difficulty with it and consider multiple options:

#. Maximize for Point 5 inflow?
#. Maximize for Point 0 outflow?
#. Maximize the flow from 0 to 5 and disregard the indirect flows into 5?

Even though the latter examples are clearly wrong and an LLM should be able to account for it, it is exactly these kind
of small nuggets of confusion that compound together to an output that is overall less precise. Unfortunately, the
current generation of LLMs will not tell you the degree of confusion under which they are generating a response.

A very simple solution for this is proposed in the Good example: **keep things simple**.

Supply all necessary (dummy) data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about supply all necessary (dummy) data


.. _pitfalls:

Technical Issues
----------------
Working with LLM is currently fraught with inconsistent technical behavior. For instance, ChatGPT
has a number of very cool integrations that we can make use of, however, very often they intermittently
don't work. Often the best remedy is to try again, or in some cases, just come back later.

LLM is generating code but not executing it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you instruct the LLM to execute code, it should be able to comply and generate code into an environment
that can execute it. However, it can happen that code is generated without it being executed.

This can mean two things:

1. The LLM thinks it can get away with just generating code and not executing it, assuming you will execute the code on your own machine. In many cases, the solution to this is to nudge the LLM to: ``execute the code``.
2. The LLM is experiencing technical difficulties and cannot access its code execution environment. In this case telling it to ``execute the code`` might result in a response like ``It seems that I am currently unable to execute the code directly``. It can also happen that it is not able to do this introspection and it will ignore your request and blindly regenerating the code again with, again, skipping the execution. It could even emit an error message like:

.. code-block:: console

   It seems that I am currently unable to execute the code directly

Both behaviors listed in 2. are often solved by either starting a new conversation and trying again, or waiting for a
while until the issues are resolved.

The LLM cannot install the wheel or cannot read attached data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the LLM prompts you to install a wheel or attach a data file which you have already attached, it is likely
an intermittent system issue. The LLM could also tell you that it is not able find the required file:

.. code-block:: console

   I cannot find the .whl feel you are trying to install


In many cases can be solved by starting a new chat window, or, as stated previously, wait for the system issue to be
resolved.

Modelling Pitfalls
------------------
The one thing to always keep in mind is that almost never will the LLM express any doubts about interpreting your question. It will make assumptions and when generating an answer will try to sound authoritative.
This is why you have to make extra sure that you don't fall for any of the pitfalls that lead to bad results, since it might not be obvious where the error lies that tripped up the model.

It is all about removing as many impediments for the LLM as possible, so it can focus on the problem at hand.


Messy problem statement
^^^^^^^^^^^^^^^^^^^^^^^

Typos
"""""
If you confuse a ``0`` with a ``O``, the model might or might not be able to understand what you mean

Mixing data types
"""""""""""""""""
Having both integers and floats in your data definition is......

Too long problem statement
^^^^^^^^^^^^^^^^^^^^^^^^^^
Might be fixed with longer context windows

Too many constraints
""""""""""""""""""""
Too many constraints

Too much inline data
""""""""""""""""""""
Our experimentation found that LLMs can work with a surprisingly wide variety of formatted data, csv, markdown, LaTeX,
and others it can often read with no problem. Where it does start to become problematic is too much inline data as they
represent tokens that it will need to be taken into account into the full context.

Our recommendation is that if you have more than 10 lines of data, it should be stored into a data file that is uploaded
with the prompt.

Too many different data collections
"""""""""""""""""""""""""""""""""""
Too many different data collections

Too much preprocessing on the data
""""""""""""""""""""""""""""""""""
Too much preprocessing on the data

Advanced Gurobipy API's
^^^^^^^^^^^^^^^^^^^^^^^
More training is done on the earlier ``gurobipy`` API's. This is not a problem since the ``gurobipy`` API is quite stable.
However, it does mean that the LLM is less prone to using the newest advanced API's which allow for building models with more complex constraints.
For simple models however, these advanced API's should not be needed.

Too much gurobipy output
^^^^^^^^^^^^^^^^^^^^^^^^
In some cases you might need to solve a large number of models. For instance, when solving a model multiple times while
varying the value of a constant (in a strategy called an "efficient frontier"). We show this in the
:ref:`portfolio <portfolio>` example.

This can lead to a large amount of logging output from Gurobi. Especially if you work with a platform like ChatGPT,
which can run the code within Code Analysis blocks, this will consume a large number of tokens and could lead to
adverse effects. For such cases we recommend instructing the LLM to suppress logging output (which should add
``model.setParam("OutputFlag", 0)`` to the resulting code).

Avoid abstract concepts
^^^^^^^^^^^^^^^^^^^^^^^
TODO: It cannot think in 3D.
