#!/usr/bin/python3
"""Module that contains the add_integer function."""


def add_integer(a, b=98):
    """Add two integers or floats (floats are cast to int)."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Handle NaN (a != a) and Infinity/Overflow (abs(a) == float('inf'))
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)
