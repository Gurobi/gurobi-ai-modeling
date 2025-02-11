Supply all necessary (dummy) data
---------------------------------
As alluded to in the previous paragraphs, the current generation of LLMs will not tell the degree of uncertainty it
is generating the response under. Because of this, if you forget to supply any data, be it a single column or the whole
data set, it will not prompt you or express confusion.

It might either adapt its interpretation of the problem and leave out some important aspect that requires that data, or
it might generate some dummy data on its own accord without asking you.

Obviously, one should exercise restraint about supplying proprietary or private data to commercial LLMs. We therefore suggest
creating a dummy or anonymized dataset.

Dos and don'ts for data files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We found that there are some patterns that if embedded in a data file, trips up various LLMs. One example is: ``(%)``.
For instance, we used to have the following table:

.. list-table::
   :header-rows: 1

   * - Backend Service
     - Internal Gateway
     - Additional Processing Time (ms)
     - Additional Reliability (%)
   * - A
     - F
     - 50
     - 99.8
   * - A
     - G
     - 60
     - 99.7
   * - A
     - H
     - 55
     - 99.9


We have noticed multiple different LLMs omitting the ``(%)`` in ``Additional Reliability (%)`` when generating code
utilizing this table. What is strange is how consistent this behavior is across retries and also across the different
LLM vendors. We suggest that for now, avoiding this string in any of your prompts or data files. If you find any
other such error inducing string, we'd love to hear from you!
