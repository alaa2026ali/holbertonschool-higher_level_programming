#!/usr/bin/env python3
"""Mixins and Dragon class"""


class SwimMixin:
    """Provides swimming ability"""

    def swim(self):
        """Swim method"""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability"""

    def fly(self):
        """Fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""

    def roar(self):
        """Roar method"""
        print("The dragon roars!")
