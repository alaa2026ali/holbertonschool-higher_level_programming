#!/usr/bin/python3
"""Module that contains the add_integer function."""

import math


def add_integer(a, b=98):
    """Add two integers or floats (floats are cast to int)."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise TypeError("a must be an integer")

    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
