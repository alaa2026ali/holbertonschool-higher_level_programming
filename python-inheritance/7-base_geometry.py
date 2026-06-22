#!/usr/bin/python3
"""
This module contains the BaseGeometry class with area and validation methods.
Each class and method must have comprehensive docstring documentation.
"""


class BaseGeometry:
    """A base class for geometry-related objects with validation capabilities."""

    def area(self):
        """Raises an Exception indicating that the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given value is a strictly positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
