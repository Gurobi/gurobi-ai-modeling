I don't understand how hosting applications works
=================================================

.. include:: /_static/feedback.rst

We saw this example in the :ref:`tips_and_pitfalls` section already. It might be quite difficult for an LLM to reason
about how a problem involving hosting in the cloud works and more hand holding is currently required.

Of course, the LLM very likely does know about how cloud hosting works. So it's not unreasonable to think that the LLM
should be able to figure out what are the implications of this for the model formulation. However, we found that the
LLMs are currently unlikely to convert this knowledge into correct constraints. The reason for this is likely that the
LLM has (almost) never seen a problem like this before and it cannot easily rehash from existing sources.

What would actually be needed is some intermediate steps by the LLM and think about the implications of the domain.
We think that future versions of LLMs will be more competent at doing this, but the current available models seem to
need some help from the user.

As shown in the :ref:`tips_and_pitfalls` section. One should be very specific about what this means for how to problem
should be approached.

.. note::

   As it happens, OpenAI recently released the ``o1-preview`` model which seems to be effective at exactly this
   reasoning step!
