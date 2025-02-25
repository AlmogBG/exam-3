import math
import numpy as np
import matplotlib.pyplot as plt

import sympy as sp

#from colors import bcolors
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')
def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    return integral
def calculate_error(f, a, b, n):
    h = (b - a) / n
    x_values = [a + i * h for i in range(n+1)]
    max_derivative_4 = max(abs(f(x).diff(x, 4).subs(x, xi)) for xi in x_values)
    error = (1/180) * h**4 * (b - a) * max_derivative_4
    return error

if __name__ == '__main__':
    f = lambda x: (2*x**2+np.cos(2*np.e**-2**x))/(2*x**3+x**2-6)
    n = 4
    a=-1.4
    b=1.1

    print( f" Division into n={n} sections ")
    integral = simpsons_rule(f, a, b, n)
    error = calculate_error(f, a, b, n)
    print( f"Numerical Integration of definite integral in range [{a},{b}] is {integral}")
    print(f"Error is {error}")
