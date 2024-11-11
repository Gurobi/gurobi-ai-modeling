Other modeling Pitfalls
-----------------------
The one thing to always keep in mind is that almost never will the LLM express any doubts about interpreting your question. It will make assumptions and when generating an answer will try to sound authoritative.
This is why you have to make extra sure that you don't fall for any of the pitfalls that lead to bad results, since it might not be obvious where the error lies that tripped up the model.

It is all about removing as many impediments for the LLM as possible, so it can focus on the problem at hand.

Below you can find a few small ways in which you can trip up the LLM:

Typos
^^^^^
Confusing a ``0`` (zero) with an ``O`` (capital o).

Mixing data types
^^^^^^^^^^^^^^^^^
Mixing both integers and floats in a column in your dataset is likely to be successfully parsed and handled by the LLM, but given this section's preamble, it's advised to stay consistent.

Too much inline data
^^^^^^^^^^^^^^^^^^^^
Our experimentation found that LLMs can work with a surprisingly wide variety of formatted data, csv, markdown, LaTeX,
and others it can often read with no problem. Where it does start to become problematic is too much inline data as they
represent tokens that it will need to be taken into account into the full context.

Our recommendation is that if you have more than 10 lines of data, it should be stored into a data file that is uploaded
with the prompt.

Data preprocessing
^^^^^^^^^^^^^^^^^^
In many cases you can supply raw data to the LLM and instruct it how to preprocess it and extract meaning from it.
However, any of these steps add complexity to the overall problem, it is therefore advised to do the preprocessing
of the data and extracting of features so that the LLM focus on the optimization problem in isolation.