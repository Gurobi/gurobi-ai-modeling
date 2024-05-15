Example prompts
===============

This section documents the Gurobi C interface. This manual begins with a
quick overview of the functions in the interface, and continues with

If you are new to the Gurobi Optimizer, we suggest that you start with
These documents provide concrete examples of how to use the routines described here.

.. rubric:: Environments

The first step in using the Gurobi C optimizer is to create an
environment, using The environment acts
as a container for all data associated with a set of optimization runs.
You will generally only need one environment in your program, even if
you wish to work with multiple optimization models. Once you are done
with an environment, you should c
associated resources.