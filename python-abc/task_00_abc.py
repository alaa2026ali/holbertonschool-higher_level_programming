#!/usr/bin/env python3
"""Abstract Animal class and subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class"""

    @abstractmethod
    def sound(self):
        """Return animal sound"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
