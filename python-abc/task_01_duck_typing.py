#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class defining the interface for all shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the shape."""
        pass

class Circle(Shape):
    """Concrete Shape representing a circle."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Concrete Shape representing a rectangle."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print area and perimeter of any object that behaves like a Shape.
    Uses duck typing - we don't check isinstance, we just trust it has
    area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
