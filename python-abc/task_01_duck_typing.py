#!/usr/bin/python3
"""Task 01 - Duck Typing"""

from math import pi


class Circle:
    """Circle class"""

    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return pi * (abs(self.radius) ** 2)

    def circumference(self):
        """Return the circumference of the circle"""
        return 2 * pi * abs(self.radius)
