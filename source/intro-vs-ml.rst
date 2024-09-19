Mathematical Optimization vs Machine Learning
===================================================================

.. include:: /_static/feedback.rst

Machine Learning and everything that falls under it (deep learning, large language models) are very well-known terms in data science and are powerful tools solving tons of interesting problems data scientists are tasked with. But there is a fundamental gap in what these tools can do and what organizations need. It’s not only extremely valuable to get a better understanding of what comes next (i.e. a prediction via machine learning) but what actions to take for extremely complex decisions given this future. That is where mathematical optimization excels – it is a prescriptive tool. 

Machine learning and mathematical optimization differ in approach, purpose, and methodology as they are meant to solve different problems. Understanding these differences is key to applying each technique effectively in real-world problems.

Mathematical Optimization is a Prescriptive Approach for Decision-Making
-----------------------------------------------------------

Mathematical optimization is inherently prescriptive.  Its goal is to find the best possible, and mathematically proven, decision given an objective and constraints which you define to represent your real-life problem. 

- **Declarative Nature**: You state the goal (e.g., maximize profit, minimize cost) and constraints (e.g., budget limits, resource capacities), and define the kinds of choices you have available to influence these (e.g. which ads to run on social media). It is then the job of the optimization solver to determine the optimal solution.
- **Complex, Fast Decision-Making**: Mathematical optimization is particularly suited for making large-scale, fast decisions in complex environments. Areas in which optimization is commonly used include logistics, finance, supply chain management, and scheduling.

Machine Learning is Excellent at Predictive Modeling
------------------------------------------

Machine learning, on the other hand, is very commonly used as a predictive tool. It involves training models on historical data to make predictions or classify new data points. There are definitely declarative elements when it comes to programming in machine learning, but the process of training a model can often involve explicitly defining the steps algorithms should take.

- **Imperative Nature**: You define the model structure, the training process, and how data flows through the model. There is a lot of emphasis on specifying the steps required to learn from data.
- **Use Cases**: Widely used in tasks such as image recognition, natural language processing, and recommendation systems, where the goal is to learn patterns from historical data.

To Sum Up, There are Big Differences
-------------------

1. **Prescriptive vs. Predictive**: Mathematical optimization prescribes the best course of action to achieve a specific goal, while machine learning predicts outcomes based on patterns in the data.
2. **Goal vs. Process**: In mathematical optimization, you declare the decision types, contraints, and objective and let the solver find the solution. In machine learning, you define a process that the model follows to learn from data.
3. **Use of Data**: Machine learning relies heavily on a lot of data to make predictions, classifications, etc., while mathematical optimization uses data as values within a defined mathematical model. For example, the estimated cost of shipping something from a manufacturing facility to a warehouse, or the likelihood a customer will churn can be inputs to an optimzation model. And these are things machine learing is great at estimating!
4. **These are Complementary Tools**: Predictions and decsions made using them are not the same thing. While some decisions may be easy; if rain is predicted tomorrow you probably won't go for a bike ride, many others businesses face are much more complex. As described in the last point, there are numerous ways machine learning and optimization can and should work together. 

Both mathematical optimization and machine learning are invaluable in solving complex problems, but they approach these problems very differently. Machine learning can take massive amounts of data and discover patterns and relationships previously undiscoverable to help build predictions. Mathematical optimization's prescriptive nature makes it great for fast decision-making in complex spaces, where the objective and constraints are well-defined.

Choosing the right tool depends on the problem at hand and the desired outcome.
