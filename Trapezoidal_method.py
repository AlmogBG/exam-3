import math
import sympy as sp
import numpy as np
#from colors import bcolors
x = sp.symbols('x')

def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return integral
def calculate_error_trapezoidal(f, a, b, n):
    h = (b - a) / n
    x_values = [a + i * h for i in range(n+1)]
    max_derivative_2 = max(abs(f(x).diff(x, 2).subs(x, xi)) for xi in x_values)
    error = (1/12) * h**2 * (b - a) * max_derivative_2
    return error

if __name__ == '__main__':
    f = lambda x:(2*x**2+np.cos(2*np.e**-2**x))/(2*x**3+x**2-6)
    result = trapezoidal_rule(f, -1.4, 1.1, 20)
    error = calculate_error_trapezoidal(f, -1.4, 1.1, 20)
    print(f"Approximate integral: {result:.5f}")
    print("Error is",error)