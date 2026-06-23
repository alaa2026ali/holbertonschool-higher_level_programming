#!/usr/bin/env python3
"""
Module defining geometric shapes and utility functions.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Representation of a circle shape.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle instance with a given radius.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Compute the area of the circle.
        """
        return pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """
        Compute the perimeter of the circle.
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Representation of a rectangle shape.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle instance with width and height.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Compute the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Compute the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape: any) -> None:
    """
    Print the area and perimeter of a given shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
