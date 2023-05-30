#!/usr/bin/python3
"""The square class is created just to permit"""


class Square:
    """Setting private size data"""
    pass

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
