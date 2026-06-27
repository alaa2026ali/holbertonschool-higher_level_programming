#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print the area and perimeter of any shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
