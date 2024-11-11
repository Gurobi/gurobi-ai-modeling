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