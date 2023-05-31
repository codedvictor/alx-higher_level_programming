#!/usr/bin/python3
import math


class MagicClass:
    """create a circle class"""

    def __init__(self, radius=0):
        """Initialization"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area of circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference of circle"""
        return math.pi * 2 * self.__radius
