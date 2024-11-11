Modeling
========

As mentioned in the previous chapter, Mathematical Optimization relies on modeling, and this type of modeling is often more involved than modeling with Machine Learning.

To create an optimization model, one first needs to describe the optimization problem and convert this into mathematical
formulation or code before it can be solved. The mathematical language used to translate a problem description into an
optimization model is well defined - this is the realm of Operations Research (OR) and Mathematical Programming.
Below, we review the key elements of this process.

The Problem Statement
---------------------
Problem statements are the foundation of any optimization application. The benefits of devoting time to crafting a good problem statement for your application include:

- Aligning multiple stakeholders and setting expectations
- Identifying any competing objectives
- Documentation around your application

A well-posed problem statement should include all of the key components of an optimization model, including information about:

- Which decisions are being made?
- What constraints or restrictions must be satisfied for the decisions to be considered feasible?
- How can we identify the best among alternative feasible decision outcomes? Are we trying to minimize or maximize something?

Although a problem statement need not explicitly contain mathematical notation, inequalities or functions, having a precise and complete description of the above information will make it easier for a human (or AI agent) to construct a mathematical model that accurately represents the decision problem.

In most cases, data should be separated from the model, allowing the problem to be defined in a general or abstract way (e.g., `Determine how much of each product should be produced at each facility.`).
Then, after a mathematical model is constructed, specific sets of data (e.g., a spreadsheet or text file containing a list of facilities, a list of products, cost and demand data) can be loaded as input to construct and solve individual instances of the decision problem.

Separation of the abstract problem description and problem problem data allows problems to be more simply stated, and reused with different data sets.

Components of an Optimization Model
-----------------------------------
Understanding the key components of an optimization model is critical when creating or reviewing a model. The main components of an optimization model are:

- **Decision Variables:** The set of variables representing choices that must be made.  For example, 'production rate' or 'machine on/off status'. Note that a variable's allowed set of values can be continuous (eg., ``1.034``, ``938.33``), integer (eg., ``1``, ``34``), or binary (ie. ``0`` or ``1``).
- **Constraints:** Constraints define relationships between the values of the variables that must be satisfied for a set of decisions to be considered feasible. They can represent limitations that must be accounted for, and criteria that must be satisfied. For example: `no more than 3 workers scheduled on any day` or `at least 100 units in inventory at all times`.
- **Objective:** The goal of your application. For example: `minimize cost` or `maximize reliability`.
- **Parameters and Data:** The input data required to make the model represent exactly the situation at hand.  For example: a table with the price of different foodstuffs for every month of the year.

Further educational resources for learning about optimization, model writing, and how the
`algorithms <https://www.gurobi.com/resources/mixed-integer-programming-mip-a-primer-on-the-basics/>`_
work are listed in the :ref:`Educational Resources <education>` chapter.

Translation of Problem Statement into Mathematical Formulation: Two Options
--------------------------------------------------------------------------------
Historically, solving an optimization model would involve an optimization expert developing a mathematical model from a
problem statement, implementing that model in code, and running the code to produce solutions. With the advent of LLMs,
we might now have a new viable approach for transforming a problem statement into a mathematical optimization model and code.

However, one should exercise discretion. With the current generation of LLMs some of the human tact and intuition are
missing from the equation, making crafting an accurate and complete problem statement especially important, as the
prompt will be the basis for all output.

Review, Validate and Iterate
-------------------------------
Whether the model was constructed by a human expert or LLM, we will still need to review the results.
One component of this is to review the description and implementation of the model to make sure that it includes all key components: do the variables defined in the model account for all decisions that must be made? Are all constraints in the problem description encoded in the model? Do the output solutions make sense?

Once it has been validated that the model and output accurately represent and solve the initial problem, a next step is to investigate whether or not the *intended* problem was accurately described in the initial problem statement.
At this step we may find that the original problem statement was missing an important constraint or consideration and must be amended, this process can be iterated until the desired results are achieved.

In some cases, common-sense structural constraints such as `a machine cannot process multiple jobs at the same time` or `a worker must travel to the job site before starting the job` can be overlooked by a human modeler, or LLM, requiring modification of the model or prompt to ensure their inclusion.
In cases where a prompt is ambiguous, the LLM is likely to make its best guess regarding some structural constraints, and its guesses may not be aligned with the intentions of the user.

Mistakes could appear at any step of the process and more detailed suggestions for troubleshooting models can be found in the :ref:`Testing` section.

.. note::
    In practice, the knowledge about the full business process is usually not located with a single person or group, but scattered among larger parts of the organization. Hence, it is common that more and more aspects of the business application enter the problem statement when the model solution gets reviewed by additional stakeholders.
