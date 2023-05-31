#!/usr/bin/python3
"""The square class is created just to permit"""


class Square:
    """Setting private size data"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """initialize object variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple or type(position[0]) is not int or
                type(position[1]) is not int or len(position) != 2 or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    def area(self):
        """calculate area of square"""
        size = self.__size
        return size * size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or value[0] < 0
                or value[1] < 0 or type(value[0]) is not int
                or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
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
