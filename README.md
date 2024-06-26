# opn Library

## Overview

The opn Library is a Python package that defines a special numerical domain called OPNs (Ordered pair of normalized real numbers). This library implements custom arithmetic operations, including addition, subtraction, multiplication, division, exponentiation, root extraction, and trigonometric functions, all following the unique rules of the OPNs domain.

## Features

- Custom OPNs arithmetic operations
- OPNs class
- OPNs-specific math functions

## Installation

To install the OPNs Library, clone this repository:

```bash
git clone https://github.com/alvinzean/opn.git
cd opn
```

## Usage

- ### OPNs Class(opn.py)
The **OPN** class includes the definition of OPNs and their basic operations. It overrides the standard arithmetic operators to support custom rules.

#### Basic OPNs Operations

```python
from opn import OPN

a = OPN(3, 4)
b = OPN(-3, -4)

print(a + b)  # OPNs addition
print(a - b)  # OPNs subtraction
print(a * b)  # OPNs multiplication
print(a / b)  # OPNs division
print(a ** 2) # OPNs exponentiation
print(a == b) # OPNs comparison
print(a < b)  # OPNs less than
```

- ### OPNs Math Functions(opn_math.py)
The **opn_math** module provides various mathematical functions for OPNs, similar to Python's math library. It includes functions for logarithms, trigonometric functions, and more (will be continuously updated).

#### Example Usage

```python
from opn import OPN
import opn_math

a = OPN(3, 4)

print(opn_math.log(a))     # OPNs logarithm
print(opn_math.sin(a))     # OPNs sine
print(opn_math.asin(a))    # OPNs arcsine
print(opn_math.exp(a))     # OPNs exponential
```

## OPNs Mathematical Formulas

An OPNs is defined as $\alpha=(\mu_{\alpha}, \nu_{\alpha})$, with both $\mu_{\alpha}$ and $\nu_{\alpha}$ in the interval (0,1). In the actual operation, we removed the restriction of two terms in OPNs with values between 0 and 1. Here are some examples of mathematical formulas for OPNs:

- ### Addition

Given two OPNs, $\alpha=(\mu_{\alpha}, \nu_{\alpha})$ and $\beta=(\mu_{\beta}, \nu_{\beta})$, their addition is defined as:

$$\alpha+\beta=(\mu_{\alpha}+\mu_{\beta}, \nu_{\alpha}+\nu_{\beta})$$

- ### Multiplication

The multiplication of two OPNs is defined as:
$$\alpha\cdot\beta = (-\mu_{\alpha}\nu_{\beta}-\nu_{\alpha}\mu_{\beta},-\mu_{\alpha}\mu_{\beta}-\nu_{\alpha}\nu_{\beta})$$

- ### Exponentiation

The exponentiation of an OPN $\alpha$ raised to the power of $n$ is defined as:
$$\alpha^{n} = \left (\frac{(-1)^{n+1}}{2} \left ( \mu_{\alpha} + \nu_{\alpha} \right )^n + \frac{1}{2}\left ( \mu_{\alpha} - \nu_{\alpha} \right )^n, \frac{(-1)^{n+1}}{2} \left ( \mu_{\alpha} + \nu_{\alpha} \right )^n - \frac{1}{2}\left ( \mu_{\alpha} - \nu_{\alpha} \right )^n  \right )$$

For more detailed OPNs calculation rules, please refer to the paper "Ordered Pair of Normalized Real Numbers" by Lei Zhou.

## Future Updates

We are committed to better extending the OPN library to machine learning development. We are continuously working on improving the OPNs Library. Upcoming features include:

- Matrix class for OPNs
- A Numpy-like library for OPNs
Stay tuned for these updates!




