#!/usr/bin/python3
"""test cases package"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestBaseMethods(unittest.TestCase):
    """Test Base class methods"""

    def setUp(self):
        """SetUp test method"""
        Base._Base__nb_objects = 0

    def test_id_default(self):
        """default id test"""
        newid = Base()
        self.assertEqual(newid.id, 1)

    def test_id(self):
        """Test the id with int"""
        newid = Base(1)
        self.assertEqual(newid.id, 1)

    def test_multiple_id(self):
        """test id with multiple class instance"""
        newid = Base()
        new2 = Base()
        new3 = Base(98)
        new4 = Base()
        self.assertEqual(newid.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 98)
        self.assertEqual(new4.id, 3)

    def test_id_string(self):
        """ Test string id"""
        new = Base("1")
        self.assertEqual(new.id, "1")

    def test_2_args_id(self):
        """Test 2 args id for init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attr(self):
        """Test accessing the private attr"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_to_json_string(self):
        """ Test Dictionary to JSON string """
        r = Rectangle(2, 2)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(json_dictionary)
            self.assertEqual(std_out.getvalue(), res.replace("'", "\""))

    def test_save_to_file(self):
        """ Test save to file """
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), res)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test save to file """
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), res)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 98}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 98)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 98, 'width': 1}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 98)
        self.assertEqual(r.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 98)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2, 'x': 3}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 98)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 98, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 98)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
