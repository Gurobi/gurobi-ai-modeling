Unexpected prompts can lead to unexpected behavior
--------------------------------------------------
You might remember that an LLM is just statistically reciting tokens it has seen before. If your prompt is doing
something that the LLM deems `unexpected`, it might cause it either:

1. blindly follow your instructions, or
2. exert behavior that looks like it assumes you made a mistake and just selectively augments part of your prompt.

To illustrate this, in one of our Examples, there used to be an equation for calculating total shipping costs on an
E-commerce platform:

.. code-block:: console

   - Total Shipping costs: SC = Base Shipping Cost+(2×Size (kg))+(1.5×Weight (kg))

It states the total shipping costs depends on a base cost and weight of the item category. We actually forgot to mention
that the number of shipped products should also be included. We found that the LLM ended up being confused by this and
exerting non-deterministic behavior, sometimes adding the number of products, sometimes leaving it as is, and sometimes
coming up with something else entirely. From its behavior, it seemed that it was somehow `expecting` the number of
items shipped to be part of the equation.

This is where your knowledge of the problem comes in. If the shipping cost indeed should depend on the number of items
shipped, it should be reflected in the equation:

.. code-block:: console

   - Shipping costs: SC = Base Shipping Cost + ((2×Size (kg))+(1.5×Weight (kg)) * units sold)

If it is somehow not dependent on the number of items shipped, we can improve the prompt a little bit by stating this
fact explicitly:

.. code-block:: console

   - Shipping costs: SC = Base Shipping Cost+(2×Size (kg))+(1.5×Weight (kg)). The total shipping cost is independent on the number of items shipped.