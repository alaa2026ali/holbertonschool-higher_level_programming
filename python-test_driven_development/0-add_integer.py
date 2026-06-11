#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles type validation, including float overflow and NaN checks.
"""
import math


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, defaults to 98).

    Raises:
        TypeError: If a or b are not integers/floats, or if they are NaN/Inf.

    Returns:
        The addition of a and b as an integer.
    """
    # Validate 'a' for valid type, NaN, and Infinity (Float overflow)
    if not isinstance(a, (int, float)) or math.isnan(a) or math.isinf(a):
        raise TypeError("a must be an integer")

    # Validate 'b' for valid type, NaN, and Infinity (Float overflow)
    if not isinstance(b, (int, float)) or math.isnan(b) or math.isinf(b):
        raise TypeError("b must be an integer")

    # Cast floats to integers as required by the specifications
    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
