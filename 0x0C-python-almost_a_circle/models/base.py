#!/usr/bin/python3
"""Write a class base"""


class Base:
    """Base class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """initial declaraction of self & id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
