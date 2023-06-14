#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class with 3 publics attributes"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attibutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student"""

        ret = self.__dict__

        if type(attrs) is list:
            for att in attrs:
                if type(att) is not str:
                    return ret

            att_dict = {}
            for att in attrs:
                for x in ret:
                    if att == x:
                        att_dict[att] = ret[att]

            return att_dict

        return ret
