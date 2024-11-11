Correct usage of gurobipy
-------------------------


Avoid usage of recent gurobipy API's
====================================
Most of the data utilized for training the current generating of LLMs contain data using earlier versions of ``gurobipy``
API's. This is generally not a problem since the ``gurobipy`` API is quite stable (this is by design). However, it does
mean that the LLM is less prone to using the newest advanced API's which allow for building models with more complex
constraints like quadratic or nonlinear constraints. For simple models however, these advanced API's should
not be needed.

Too much gurobipy output
========================
In some cases you might need to solve a large number of models. For instance, when solving a model multiple times while
varying the value of a constant (eg. in a strategy called a `Pareto Front <https://en.wikipedia.org/wiki/Pareto_front>`__
or `efficient frontier`). We show this in the :ref:`portfolio <portfolio>` example.

This can lead to a large amount of logging output from Gurobi. Especially if you work with a platform like ChatGPT,
which can run the code within Code Analysis blocks, this will consume a large number of tokens and could lead to
adverse effects. For such cases we recommend instructing the LLM to suppress logging output (which should add
``model.setParam("OutputFlag", 0)`` to the resulting code).