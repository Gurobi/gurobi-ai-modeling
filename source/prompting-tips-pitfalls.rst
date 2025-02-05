.. _tips_and_pitfalls:

Tips and pitfalls
==================

During the course of this project and formulating the :doc:`prompting-examples` section, we have come across common tips
and pitfalls relating to prompting and handling LLMs in general. In the current section we will share our findings that
relate to modeling optimization problems using LLMs and help set you up for prompting success.

.. toctree::
   :maxdepth: 1

   tips_pitfalls/unambiguous
   tips_pitfalls/unexpected
   tips_pitfalls/divisible_variables
   tips_pitfalls/unnecessary
   tips_pitfalls/supply_data
   tips_pitfalls/technical_issues
   tips_pitfalls/gurobipy
   tips_pitfalls/other

Examples of LLM Reasoning limitations
-------------------------------------

.. _case_studies:

In many cases, LLMs have impressed us with their technological prowess. In arguably more cases, they have surprised us
with their interesting mishaps. It is difficult to pinpoint exactly why an LLM gets something wrong. Moreover,
an LLM getting something wrong can often catch us by surprise. In this chapter we will share a few case studies where we
were caught off-guard by its inability to generate a correct model.

.. note::

   In the time since writing this section, OpenAI recently released the ``o1`` model, and recently ``o3-mini`` models.
   In our testing of ``o1``, we found that ChatGPT is able to solve practically all use cases discussed
   in the coming sections (and expect no less of ``o3-mini``). We will leave the current pages in place not only because
   ``o1`` and ``o3-mini`` do not yet support Code Interpreter or Custom GPTs, but because we think it still gives a
   valuable insight into how LLMs sometimes upend our expectations.

.. toctree::
   :maxdepth: 2

   ../case_studies/supply-demand
   ../case_studies/temporal-complexity
   ../case_studies/3d-space
   ../case_studies/applications-on-ec2
