Example prompts
===============

In the following pages we demonstrate a number of example applications tailored to a range of technical specialties.
Each example shows the prompt and any data files if applicable. This prompt was fed to the `Gurobi AI Modeling Assistant <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_.
Subsequently, the `Generated Model formulation` and `Generated Python code` tabs show the output of the relevant sections that
the Gurobi AI Modeling Assistant generated based on this prompt. We encourage trying out some of these example prompts to get
a feel for how the LLM generates a model (and experience how every time a slightly different model is generated with
hopefully the same resulting objective value).

We should note that the `Example generated model` outputs do not necessarily reflect Gurobi's best modeling practices. It is
merely an example of what the LLM generated for us. This example should get you on your way to solving your first
optimizing problem. As you get more comfortable with `Gurobi AI Modeling Assistant <https://chatgpt.com/g/g-g69cy3XAp-gurobi-ai-modeling-assistant>`_
and later familiarize yourself with the ``gurobipy`` API, in time, you will learn how to construct better models.

Most examples are accompanied by a solution visualization.
In each case, these were created by providing additional queries to the LLM after the model was generated and solved.
Some examples of prompts to generate visualizations are included in the :ref:`visualize` section.

Also note that not all the example prompts are created equal, meaning that some are easier for the LLM to turn into a
valid model than others. You might find that some of the examples give a correct model every time, while another
might take a few tries. This should also reinforce the idea that investigating and testing the generated model is
a critical step. We discuss how to do this in the :ref:`testing` chapter.
