#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student."""
        if type(attrs) is list:
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""
        for key, value in json.items():
            setattr(self, key, value)
