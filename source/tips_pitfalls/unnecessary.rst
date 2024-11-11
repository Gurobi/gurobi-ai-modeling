Avoid unnecessary words or statements
-------------------------------------
If you, again, think about how an LLM works, it's all about predicting the next token based on what was given before.
The implication of this is that one should avoid adding unnecessary words lest not to confuse the LLM. Let's take an
example of a bad and good pattern. The following shows a description of the objective of a data flow problem where
data can be sent via any route through the nodes :math:`\{0,1,2,3,4,5\}`:

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         Imagine we're managing a telecommunications network that spans 6 key points, from a primary data center (Point 0) to a major user hub (Point 5).

         ...

         The objective is to find out the maximum amount of data that can be transferred from Point 0 (Data Center) to Point 5 (User Hub) per second.


   .. tab:: Good

      .. code-block:: text

         Imagine we're managing a telecommunications network that spans 6 key points, from a primary data center (Point 0) to a major user hub (Point 5).

         ...

         The objective is to find out the maximum amount of data that can be transferred to Point 5 (User Hub) per second.

For a human, the objective should be clear for either version: maximize the flow into Point 5. A machine might have more
difficulty with it and consider multiple options:

1. Maximize for Point 5 inflow?
2. Maximize for Point 0 outflow?
3. Maximize the direct flows from 0 to 5 and disregard the indirect flows into 5?

Even though option 2 and 3 might seem intuitively wrong to the human eye (and an LLM should be able to be able to
interpret it that way), it is exactly these kind of small sources of confusion that compound together with other
ambiguities in the prompt that lead to an output that is overall less precise.

A very simple solution for this is proposed in the Good example: `keep things as simple as possible`.