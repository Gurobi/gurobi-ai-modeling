Should variables be considered divisible or not?
------------------------------------------------
In many cases, the LLM will be able to deduce whether the variables involved in the problem should be divisible
or not. For instance, cars are very likely to be non-divisible (nobody wants ``0.54`` of a car), while kilograms are likely considered divisible.

However, if this is not unambiguously clear from the item itself, it will be helpful to mention how it
should be considered.

.. tabs::

   .. tab:: Bad

      .. code-block:: text

         I want to optimize my diet.

         Objective: I want to minimize the cost of food while upholding my dietary needs.

         Constraints:
         - I want to eat between 1800 and 2200 calories per day
         - At least 91 gram of protein
         - At most 65 gram of fat
         - At most 1779 mg of sodium

         ...


   .. tab:: Good

      .. code-block:: text

         I want to optimize my diet.

         Objective: I want to minimize the cost of food while upholding my dietary needs.

         Constraints:
         - I want to eat between 1800 and 2200 calories per day
         - At least 91 gram of protein
         - At most 65 gram of fat
         - At most 1779 mg of sodium
         - Portions are non-divisible

         ...
