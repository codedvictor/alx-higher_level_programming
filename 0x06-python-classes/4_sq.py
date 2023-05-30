#!/usr/bin/python3
"""The square class is created just to permit"""


class Square:
    """Setting private size data"""
    pass

    def __init__(self, size=0):
        """initialize object variable"""
        self.__size = size

    def area(self):
        """calculate area of square"""
        size = self.__size
        return (size * size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__value = value
        size = value
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
