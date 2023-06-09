#!/usr/bin/python3
"""Class to inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class from base superclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the parameters"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout"""
        rec = "\n" * self.y
        for row in range(self.height):
            rec += " " * self.x
            rec += "#" * self.width + "\n"

        print(rec[:-1])

    def __str__(self):
        """rectangle string representation"""
        rec = "[Rectangle] ({}) {}/{} - ".format(self.id, self.x, self.y)
        st = "{}/{}".format(self.width, self.height)
        return (rec + st)

    def update(self, *args, **kwargs):
        """assign args to each attr"""
        if len(args) != 0 and args is not None:
            get_attr = ['id', 'width', 'height', 'x', 'y']
            for o in range(len(args)):
                setattr(self, get_attr[o], args[o])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """get attributes from disctionary"""
        dik = {}
        get_attr = ['id', 'width', 'height', 'x', 'y']
        for key in get_attr:
            dik[key] = getattr(self, key)

        return dik
