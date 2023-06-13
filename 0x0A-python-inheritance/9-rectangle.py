#!/usr/bin/python3
"""Defines a class that inherited from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherited from BaseGeometry"""

    def __init__(self, width, height):
        """private attribute"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        """return a string rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
