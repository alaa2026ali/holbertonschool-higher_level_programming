#!/usr/bin/python3
"""Module that contains the add_integer function."""
import math


def add_integer(a, b=98):
    """Add two integers and return the result.

    Floats are cast to integers before addition.
    """
    # Reject non-numbers, infinity, or NaN values
    if type(a) not in [int, float] or math.isinf(a) or math.isnan(a):
        raise TypeError("a must be an integer")

    if type(b) not in [int, float] or math.isinf(b) or math.isnan(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
