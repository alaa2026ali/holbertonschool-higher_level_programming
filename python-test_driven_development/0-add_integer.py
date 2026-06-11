#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles type validation, including float overflow and NaN checks
without importing any modules.
"""


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
    # Validate 'a' (Check type, NaN, and Infinity)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")

    # Validate 'b' (Check type, NaN, and Infinity)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    return a + b
