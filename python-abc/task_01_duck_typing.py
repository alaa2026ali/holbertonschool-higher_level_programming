#!/usr/bin/env python3
"""
Module defining geometric shapes and utility functions.
This module includes an abstract base class Shape, along with
concrete implementations Circle and Rectangle, and a function
to display shape information.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Representation of a circle shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Compute the area of the circle using pi * r^2.
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """
        Compute the perimeter of the circle using 2 * pi * r.
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Representation of a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape.
    This function utilizes Duck Typing, accepting any object
    that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
