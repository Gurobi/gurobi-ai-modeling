Mathematical Optimization vs Machine Learning
===================================================================

.. include:: /_static/feedback.rst

One way of understanding Mathematical Optimization is by comparing it to a related, but ultimately very different
concept: Machine Learning.

Machine Learning and everything that falls under it (deep learning, large language models) are powerful tools solving
tons of interesting problems. Given a large dataset and an algorithm, it can make inferences or predictions about the
future. However, there is a fundamental gap between what these tools can do and what organizations need: it’s not only
extremely valuable to get a better understanding of what comes next (ie. prediction via machine learning), but also what
actions to take given this future. That is where mathematical optimization excels – it is a prescriptive tool.

Machine learning and mathematical optimization differ in approach, purpose, and methodology as they are meant to solve
different problems. Understanding these differences is key to applying each technique effectively in real-world problems.

Machine Learning is excellent at predictive modeling
----------------------------------------------------
Machine learning is very commonly used as a **predictive** tool. It involves training models on historical data to make
predictions or classify new data points. High-level libraries like ``scikit-learn`` and ``pytorch`` offer many
declarative constructs that help you setup a model training pipeline quickly. However, lower-level instructions to
explicitly define the algorithms' steps are also available.

- **Imperative Nature**: You define the model structure, the training process, and how data flows through the model.
  There is also a lot of emphasis on the quality and quantity of the input data.
- **Use Cases**: Widely used in tasks such as image recognition, natural language processing, and recommendation
  systems, where the goal is to learn patterns from historical data.

Mathematical Optimization is a prescriptive approach for decision-making
------------------------------------------------------------------------
Mathematical optimization, on the other hand, is inherently **prescriptive**. Its goal is to find the best possible, and
mathematically proven, decision given an objective and constraints which you define to represent your real-life problem.
Libraries like ``gurobipy`` and ``pyomo`` can be used to define the models. However, defining the model structure is
often more involved than with Machine Learning.

- **Declarative Nature**: You state the goal (e.g., maximize profit, minimize cost) and constraints (e.g., budget
  limits, resource capacities), and define the kinds of choices you have available to influence these (e.g. the pool of
  available ads to run on social media). It is then the job of the optimization solver to determine the optimal solution.
- **Use Cases**: Mathematical optimization is particularly suited for making decisions in complex environments. Areas in
  which optimization is commonly used include logistics, finance, supply chain management, and scheduling.

To sum up, there are big differences
------------------------------------
1. **Predictive vs. Prescriptive**: Machine learning predicts outcomes based on patterns in the data, while mathematical
   optimization prescribes the best course of action to achieve a specific goal.
2. **Process vs Goal**: In machine learning, you define a process that the model follows to learn from the available
   data. In mathematical optimization, you declare the decision types, constraints, and objective and let the solver
   find the solution.
3. **Use of Data**: Machine learning relies heavily on a lot of data to make predictions, classifications, etc.
   Mathematical optimization uses data as values within a defined mathematical model, for example, the estimated cost of
   shipping something from a manufacturing facility to a warehouse, or the likelihood a customer will churn.
4. **These are Complementary Tools**: Predictions and decisions are not the same thing. However, they can work in
   unison: if rain is predicted for tomorrow, you might decide to go for a bike ride today rather than tomorrow. Many
   businesses face problems that are much more complex, but at the root follow the same pattern. There are numerous ways
   machine learning and optimization can, and should, work together.

Choosing the right tool depends on the problem at hand and the desired outcome.
