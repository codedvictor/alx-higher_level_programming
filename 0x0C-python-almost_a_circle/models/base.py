#!/usr/bin/python3
"""Write a class base"""
import json
import os
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filen = "{}.json".format(cls.__name__)
        list_dik = []

        if not list_objs:
            pass
        else:
            for j in range(len(list_objs)):
                list_dik.append(list_objs[j].to_dictionary())

        lists = cls.to_json_string(list_dik)

        with open(filen, 'w') as fl:
            fl.write(lists)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialises in CSV file"""
        filen = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            list_dik = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dik = [0, 0, 0, 0]
            list_keys = ['id', 'size', 'x', 'y']

        mat = []
        if list_objs:
            for obj in list_objs:
                for l in range(len(list_keys)):
                    list_dik[l] = obj.to_dictionary()[list_keys[l]]
                mat.append(list_dik[:])

        with open(filen, 'w') as fl:
            writer = csv.writer(fl)
            writer.writerows(mat)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialises the CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            list_rows = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        mat = []
        for row in list_rows:
            dic_row = {}
            for elt in enumerate(row):
                dic_row[list_keys[elt[0]]] = int(elt[1])
            mat.append(dic_row)

        list_objs = []
        for i in range(len(mat)):
            list_objs.append(cls.create(**mat[i]))

        return list_objs
