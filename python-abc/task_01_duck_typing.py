#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class representing a geometric shape."""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
        
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

class Circle(Shape):
    """Concrete implementation of a Circle shape."""
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
        
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Concrete implementation of a Rectangle shape."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing."""
    # No type checking or isinstance calls are used here.
    # We directly call the required methods, trusting the object adheres to the interface.
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
