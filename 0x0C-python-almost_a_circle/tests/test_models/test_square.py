#!/usr/bin/python3
"""Class square methods test"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestSquareMethods(unittest.TestCase):
    """Test suite for Square class methods"""

    def setUp(self):
        """setUp class method"""
        Base._Base__nb_objects = 0

    def test_square_1_arg(self):
        """1 arg test"""
        s = Square(3)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_square_args(self):
        """all args test"""
        s = Square(2, 2, 3, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_squares(self):
        """2 squares test"""
        s = Square(1)
        s2 = Square(1)
        self.assertEqual(False, s is s2)
        self.assertEqual(False, s.id == s2.id)

    def test_is_Rect_instance(self):
        """Test square is a Rectangle instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Rectangle))

    def test_is_Base_instance(self):
        """Test square is a Base instance"""
        s = Square(1)
        self.assertEqual(True, isinstance(s, Base))

    def test_0_arg(self):
        """Test with 0 args"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_5_args(self):
        """Test with 5 args"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_access_width(self):
        """Test accessing width"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_access_height(self):
        """Test accessing height"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_access_x(self):
        """Test accessing x"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_access_y(self):
        """Test accessing y"""
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y

    def test_valid_size(self):
        """Test size string"""
        with self.assertRaises(TypeError):
            s = Square("1", 1, 2, 2)

    def test_valid_x(self):
        """Test x string"""
        with self.assertRaises(TypeError):
            s = Square(1, '1', 1, 1)

    def test_valid_y(self):
        """Test y string"""
        with self.assertRaises(TypeError):
            s = Square(1, 1, '1', 1)

    def test_size_0(self):
        """Test case of a size 0"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_neg(self):
        """Test case for x negative"""
        with self.assertRaises(ValueError):
            s = Square(1, -1)

    def test_y_neg(self):
        """Test case for y negative"""
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

    def test_size_neg(self):
        """Test case os negative size"""
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_area(self):
        """Test the return value of the area method"""
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_area_size(self):
        """Test area and update size"""
        s = Square(3)
        self.assertEqual(s.area(), 9)
        s.size = 5
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test printed string"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_display_size(self):
        """Test printed string and modified size"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.size = 3
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_dislay_xy(self):
        """Test string printed with x and y"""
        s = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.x = 1
        res = " ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

        s.y = 2
        res = "\n\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            s.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_str(self):
        """Test the __str___ return value"""
        s = Square(2)
        res = "[Square] (1) 0/0 - 2"
        self.assertEqual(s.__str__(), res)

    def test_str_2(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_3(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2, 2)
        res = "[Square] (2) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.id = 1
        s.size = 10
        res = "[Square] (1) 2/2 - 10\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_4(self):
        """Test __str__ return value"""
        s = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s2 = Square(2)
        res = "[Square] (2) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s2)
            self.assertEqual(std_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s3)
            self.assertEqual(std_out.getvalue(), res)

    def test_update(self):
        """Test update method"""
        s = Square(2)
        res = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.update(5)
        res = "[Square] (5) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_update_2(self):
        """Test update method"""
        s = Square(2)
        res = "[Square] (1) 0/0 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.update(4, 2, 2, 2)
        res = "[Square] (4) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.update(y=3)
        res = "[Square] (4) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        s.update(id=10, size=5)
        res = "[Square] (10) 2/3 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_udpate_3(self):
        """Test update method"""
        s = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        dic = {'size': 4, 'y': 2}
        s.update(**dic)
        res = "[Square] (1) 0/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

    def test_update_4(self):
        """Test udpate method"""
        s = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 2}
        with self.assertRaises(TypeError):
            s.update(**dic)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        s = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s)
            self.assertEqual(std_out.getvalue(), res)

        self.assertEqual(s.size, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(type(s.to_dictionary()))
            self.assertEqual(std_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        s1 = Square(2, 2, 2)
        res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s1)
            self.assertEqual(std_out.getvalue(), res)

        s2 = Square(5)
        res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(s2)
            self.assertEqual(std_out.getvalue(), res)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(type(s1_dictionary))
            self.assertEqual(std_out.getvalue(), res)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 98}
        s = Square.create(**dictionary)
        self.assertEqual(s.id, 98)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 98, 'size': 1}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 98)
        self.assertEqual(s.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 98, 'size': 1, 'x': 2}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 98)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 98, 'size': 1, 'x': 2, 'y': 3}
        s = Rectangle.create(**dictionary)
        self.assertEqual(s.id, 98)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, [])

    def test_save_to_file(self):
        """Test save to file"""
        Square.save_to_file([Square(1)])
        res = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
