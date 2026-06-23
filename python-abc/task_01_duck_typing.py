#!/usr/bin/env python3
"""
Module task_01_duck_typing
Defines Shape abstract base class, Circle, Rectangle, and shape_info.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape that defines the interface for geometric shapes."""

    @abstractmethod
    def area(self):
        """Public method that returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Public method that returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that implements the Shape abstract base class interface."""

    def __init__(self, radius):
        """Initializes a new instance of Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that implements the Shape abstract base class interface."""

    def __init__(self, width, height):
        """Initializes a new instance of Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any object passed to it.
    Uses duck typing instead of enforcing explicit instance checking.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
