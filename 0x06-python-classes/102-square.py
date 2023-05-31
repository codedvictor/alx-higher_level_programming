#!/usr/bin/python3
"""The square class is created just to permit"""


class Square:
    """Setting private size data"""
    pass

    def __init__(self, size=0):
        """initialize object variable"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __le__(self, val):
        return self.size <= val.size

    def __lt__(self, val):
        return self.size < val.size

    def __ge__(self, val):
        return self.size >= val.size

    def __gt__(self, val):
        return self.size > val.size

    def __ne__(self, val):
        return self.size != val.size

    def __eq__(self, val):
        return self.size == val.size
