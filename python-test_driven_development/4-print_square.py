#!/usr/bin/python3
"""
Module: 4-print_square
Function: print_square
Prints a square using the character '#'
"""


def print_square(size):
    """
    Prints a square with the character '#'.
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and not size.is_integer():
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    for _ in range(size):
        print("#" * size)
