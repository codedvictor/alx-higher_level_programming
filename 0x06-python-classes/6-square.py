#!/usr/bin/python3
"""Defines the square object class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple or len(position) != 2
                or type(position[0]) is not int or type(position[1]) is not int
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return position of Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of square"""
        if (type(value) is not tuple or len(value) != 2
                or type(value[0]) is not int or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of two positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            st = '#' * self.__size
            pt = ' ' * self.__position[0]
            for i in range(self.__size):
                print(pt, st, sep="")
