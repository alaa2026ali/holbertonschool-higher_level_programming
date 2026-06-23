#!/usr/bin/env python3
"""Module for shapes and duck typing."""

from abc import ABC, abstractmethod
import math


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
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Calculate area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
