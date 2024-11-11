Supply all necessary (dummy) data
---------------------------------
As alluded to in the previous paragraphs, the current generation of LLMs will not tell the degree of uncertainty it
is generating the response under. Because of this, if you forget to supply any data, be it a single column or the whole
data set, it will not prompt you or express confusion.

It might either adapt its interpretation of the problem and leave out some important aspect that requires that data, or
it might generate some dummy data on its own accord without asking you.

Obviously, one should exercise restraint about supplying proprietary or private data to commercial LLMs. We therefore suggest
creating a dummy or anonymized dataset.