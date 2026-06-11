#!/usr/bin/python3
"""
Module for add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        int: the sum of a and b after casting to integers

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
