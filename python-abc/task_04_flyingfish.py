#!/usr/bin/env python3
"""Fish, Bird and FlyingFish classes"""


class Fish:
    """Fish class"""

    def swim(self):
        """Fish swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """Bird flying"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class"""

    def swim(self):
        """FlyingFish swimming"""
        print("The flying fish is swimming!")

    def fly(self):
        """FlyingFish flying"""
        print("The flying fish is soaring!")

    def habitat(self):
        """FlyingFish habitat"""
        print("The flying fish lives both in water and the sky!")
