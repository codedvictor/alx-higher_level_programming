#!/usr/bin/python3
"""The square class is created just to permit"""


class Square:
    """Setting private size data"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """initialize object variable"""
        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        x = position[0]
        y = position[1]
        if (type(position) is not tuple or type(x) is not int or
                type(y) is not int or len(position) != 2 or x < 0 or y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate area of square"""
        size = self.__size
        return (size * size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        i = value[0]
        j = value[1]
        if (type(value) is not tuple or len(value) != 2 or i < 0 or j < 0 or
                type(i) is not int or type(j) is not int):
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        size = self.__size
        position = self.__position
        if size == 0:
            print('')
        else:
            st = '#' * size
            y = position[1]
            x = position[0]
            pt = ' ' * x
            for i in range(y):
                print('')
            while size:
                print(pt, st, sep="")
                size -= 1
