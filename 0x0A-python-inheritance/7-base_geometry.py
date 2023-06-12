#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry:
    """No instance"""
    pass

    def area(self):
        """No object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer confirmation"""
        if type(value) is not int:
            raise TypeError("{}  must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
