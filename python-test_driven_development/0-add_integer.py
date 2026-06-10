#!/usr/bin/python3
"""
This module contains a function that adds two integers.

The function validates input values before adding them.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
