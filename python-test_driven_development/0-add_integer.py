#!/usr/bin/python3
"""
This module provides a function to add two numbers.
It enforces type checking for integers and floats.
"""

def add_integer(a, b=98):
    """
    Adds two integers. Floats are casted to integers before addition.
    
    Raises a TypeError if either argument is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)
