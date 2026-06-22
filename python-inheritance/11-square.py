#!/usr/bin/python3
"""Module that defines Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with size."""

        super().integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
