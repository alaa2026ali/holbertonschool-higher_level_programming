#!/usr/bin/python3
"""Module for Shape, Circle, Rectangle and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize a circle."""
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
        """Initialize a rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
