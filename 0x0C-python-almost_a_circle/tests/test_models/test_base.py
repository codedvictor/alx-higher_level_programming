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
