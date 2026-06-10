#!/usr/bin/python3
"""Module that contains the add_integer function."""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Floats are cast to integers before addition.
    """
    # Check type, NaN (a != a), and Infinity without imports
    if type(a) not in [int, float] or a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")

    if type(b) not in [int, float] or b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
