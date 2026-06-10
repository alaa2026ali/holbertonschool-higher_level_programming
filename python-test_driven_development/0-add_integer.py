#!/usr/bin/python3
"""Module that contains the add_integer function."""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
