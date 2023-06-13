#!/usr/bin/python3
"""Defines a class that inherited from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Initialised the private attribute"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
