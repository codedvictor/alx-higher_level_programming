#!/usr/bin/python3
"""Write a class base"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object to file """
        filen = "{}.json".format(cls.__name__)
        list_dik = []

        if not list_objs:
            pass
        else:
            for q in range(len(list_objs)):
                list_dik.append(list_objs[q].to_dictionary())

        lists = cls.to_json_string(list_dik)

        with open(filen, 'w') as fl:
            fl.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """list of JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance creation"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """list of instances """
        filen = "{}.json".format(cls.__name__)

        if os.path.exists(filen) is False:
            return []

        with open(filen, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_obj = []

        for index in range(len(list_cls)):
            list_obj.append(cls.create(**list_cls[index]))

        return list_obj
