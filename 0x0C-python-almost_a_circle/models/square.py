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
        sq = "[Square] ({}) {}/{} -".format(self.id, self.x, self.y)
        sz = " {}".format(self.width)
        return (sq + sz)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign args to each attr"""
        if len(args) != 0 and args is not None:
            get_attr = ['id', 'size', 'x', 'y']
            for w in range(len(args)):
                if get_attr[w] == 'size':
                    setattr(self, "width", args[w])
                    setattr(self, "height", args[w])
                else:
                    setattr(self, get_attr[w], args[w])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """get attributes to dictionary"""
        dik = {}
        get_attr = ['id', 'size', 'x', 'y']
        for key in get_attr:
            if key == 'size':
                dik[key] = getattr(self, 'width')
                dik[key] = getattr(self, 'height')
            else:
                dik[key] = getattr(self, key)
        return dik
