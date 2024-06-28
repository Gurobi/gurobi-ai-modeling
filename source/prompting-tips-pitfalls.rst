Tips and pitfalls
==================

.. _tips:

Tips
-------


Unambiguous problem statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about unambiguous problem statement

.. tabs::

   .. code-tab:: text Bad

      Maximize the coverage of different test environments (EnvA, EnvB, EnvC).
      Prioritize machines that have not been tested on recently (considering the latest test_timestamp).
      Prioritize machines on which the test did not pass last time

   .. code-tab:: text Good

      Pears are green.




Supply all necessary (dummy) data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Talk about supply all necessary (dummy) data

.. _pitfalls:

Pitfalls
----------------------

The one thing to always keep in mind is that almost never will the AI model express any doubts about interpreting your question. It will make assumptions and when generating an answer will try to sound authoritative.
This is why you have to make extra sure that you don't fall for any of the pitfalls that lead to bad results, since it might not be obvious where the error lies that tripped up the model.

It is all about removing as many impediments for the AI models as possible so it can focus on the problem at hand.

LLM cannot find wheel or execute code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Depending on the LLM you are using and the number of features it has, intermittent issues might arise.
Generally speaking, the more integrated features, the higher the chance that one of these integrations intermittently fails.

If you see an error message like:

- *It seems that I am currently unable to execute the code directly*
- *I cannot find the .whl feel you are trying to install*

It is likely that your LLM provider is experiencing network issues. In such cases, trying at a later moment often solves
the problem.

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
Too much inline data

Too many different data collections
"""""""""""""""""""""""""""""""""""
Too many different data collections

Too much preprocessing on the data
""""""""""""""""""""""""""""""""""
Too much preprocessing on the data

Advanced Gurobipy API's
^^^^^^^^^^^^^^^^^^^^^^^
More training is done on the earlier ``gurobipy`` API's. This is not a problem since the ``gurobipy`` API is quite stable.
However, it does mean that the AI model is less prone to using the newest advanced API's which allow for building models with more complex constraints.
For simple models however, these advanced API's should not be needed.

Avoid abstract concepts
^^^^^^^^^^^^^^^^^^^^^^^
TODO: It cannot think in 3D.
