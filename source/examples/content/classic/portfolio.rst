.. raw:: html

    <h2>🔢 Problem Definition</h2>

Given the stock data, our goal is to determine the minimum risk portfolio and the efficient frontier.

.. raw:: html

    <h3>Step 1: Minimum Risk Portfolio</h3>

We need to formulate an optimization model to minimize the portfolio's risk (volatility), given by the portfolio variance. The portfolio variance can be expressed as:

.. math::

    \text{Variance} = \mathbf{w}^T \Sigma \mathbf{w}

where:

- :math:`\mathbf{w}` is the vector of weights of the stocks in the portfolio.
- :math:`\Sigma` is the covariance matrix of the stock returns.

The constraints are:

- The sum of the weights :math:`\mathbf{w}` should equal 1 (i.e., :math:`\sum_{i} w_i = 1`).
- The weights should be non-negative (i.e., :math:`w_i \geq 0`).

.. raw:: html

    <h3>Step 2: Efficient Frontier</h3>

The efficient frontier is obtained by varying the expected return and solving the optimization model for minimum risk. The objective function changes to:

.. math::

    \text{Variance} = \mathbf{w}^T \Sigma \mathbf{w}

Subject to:

- :math:`\sum_{i} w_i \mu_i = \mu_{\text{target}}` (Expected return constraint)
- :math:`\sum_{i} w_i = 1`
- :math:`w_i \geq 0`

where :math:`\mu_{\text{target}}` is the target return that we vary.

.. raw:: html

    <h3>Step 3: Visualization</h3>

We will plot:

- Volatility versus expected return for individual stocks.
- Volatility versus expected return for the minimum risk portfolio.
- The efficient frontier showing the volatility against expected return.
