#!/usr/bin/python3
"""Square inherit from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class functions"""

    def __init__(self, size, x=0, y=0, id=None):
        """set attibutes to parent attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """square string representation"""
        sq = "[Sqaure] ({}) {}/{} -".format(self.id, self.x, self.y)
        sz = " {}".format(self.width)
        return (sq + sz)
