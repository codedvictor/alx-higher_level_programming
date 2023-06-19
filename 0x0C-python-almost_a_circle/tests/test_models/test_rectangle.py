#!/usr/bin/python3
"""rectangle class methods test"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangleMethdods(unittest.TestCase):
    """Test suite for rectangke class methods"""

    def setUp(self):
        """setUp method"""
        Base._Base__nb_objects = 0

    def test_new_rect(self):
        """new rectangle Test"""
        rtg = Rectangle(1, 1, 1, 1, 98)
        self.assertEqual(rtg.width, 1)
        self.assertEqual(rtg.height, 1)
        self.assertEqual(rtg.x, 1)
        self.assertEqual(rtg.y, 1)
        self.assertEqual(rtg.id, 98)

    def test_new_rect_2(self):
        """Test new rectangle with default attrs"""
        rtg = Rectangle(3, 3)
        self.assertEqual(rtg.width, 3)
        self.assertEqual(rtg.height, 3)
        self.assertEqual(rtg.x, 0)
        self.assertEqual(rtg.y, 0)
        self.assertEqual(rtg.id, 1)

    def test_2_rectangles(self):
        """Test 2 new rectangles"""
        rtg = Rectangle(1, 1)
        rtg2 = Rectangle(1, 1)
        self.assertEqual(False, rtg is rtg2)
        self.assertEqual(False, rtg.id == rtg2.id)

    def test_is_Base_instance(self):
        """Test if a rectangle is a Base class instance"""
        rtg = Rectangle(1, 1)
        self.assertEqual(True, isinstance(rtg, Base))

    def test_1_arg(self):
        """Test init method with 1 arg"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1)

    def test_0_arg(self):
        """Test init method with 0 arg"""
        with self.assertRaises(TypeError):
            rtg = Rectangle()

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_access_width(self):
        """Trying to access width"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__width

    def test_access_height(self):
        """Trying to access height"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__height

    def test_access_x(self):
        """Trying to access x"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__x

    def test_access_y(self):
        """Trying to access y"""
        rtg = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rtg.__y

    def test_width_string_attr(self):
        """Test init method with a string attribute as width"""
        with self.assertRaises(TypeError):
            rtg = Rectangle("1", 1)

    def test_height_string_attr(self):
        """Test init method with a string attrubute as height"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, "1")

    def test_x_string_attr(self):
        """Test init method with a string attribute as x"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, 1, "1", 1, 1)

    def test_y_string_attr(self):
        """Test init method with a string attribute as y"""
        with self.assertRaises(TypeError):
            rtg = Rectangle(1, 1, 1, "1", 1)

    def test_width_0(self):
        """Test init method with a width = 0"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(0, 1)

    def test_height_0(self):
        """"Test init method with a height = 0"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 0)

    def test_x_neg(self):
        """Test init mehtod with negative x"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 1, -1)

    def test_y_neg(self):
        """Test init method with negative y"""
        with self.assertRaises(ValueError):
            rtg = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Test the value of the area of a rectangle"""
        rgt = Rectangle(4, 10)
        self.assertEqual(rgt.area(), 40)

    def test_area_wh(self):
        """Test the area of a rectangle with modified attrs"""
        rtg = Rectangle(4, 5)
        self.assertEqual(rtg.area(), 20)
        rtg.width = 2
        self.assertEqual(rtg.area(), 10)
        rtg.height = 10
        self.assertEqual(rtg.area(), 20)

    def test_area_2_rect(self):
        """Test the area of 2 rectangles"""
        rtg = Rectangle(2, 5)
        rtg2 = Rectangle(5, 4)
        self.assertEqual(rtg.area(), 10)
        self.assertEqual(rtg2.area(), 20)

    def test_display(self):
        """Test the printed string"""
        rtg = Rectangle(2, 3)
        res = "##\n" + "##\n" + "##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_display_wh(self):
        """Test the printed string and modify width and height"""
        rtg = Rectangle(1, 2)
        res = "#\n" + "#\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

        rtg.width = 2
        res = "##\n" + "##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_display_xy(self):
        """Test display with x and y # to default"""
        rtg = Rectangle(1, 2, 1, 1)
        res = "\n #\n #\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_display_xy1(self):
        """ Test display with x and y modified"""
        rtg = Rectangle(2, 3)
        res = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

        rtg.x = 2
        res = "  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

        rtg.y = 1
        res = "\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            rtg.display()
            self.assertEqual(std_out.getvalue(), res)

    def test_str(self):
        """Test the return value of a __str__"""
        rtg = Rectangle(2, 3)
        res = "[Rectangle] (1) 0/0 - 2/3"
        self.assertEqual(rtg.__str__(), res)

    def test_str_1(self):
        """Test the printed value of rectangle"""
        rtg = Rectangle(1, 2, 3, 4, 5)
        res = "[Rectangle] (5) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_2(self):
        """Test the printed value of rectangle without id"""
        rtg = Rectangle(1, 2, 3, 4)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg)
            self.assertEqual(std_out.getvalue(), res)

        rtg.width = 3
        rtg.height = 5
        rtg.id = 10
        res = "[Rectangle] (10) 3/4 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg)
            self.assertEqual(std_out.getvalue(), res)

    def test_str_3(self):
        """Test the printed value of rectangle"""
        rtg = Rectangle(1, 2)
        res = "[Rectangle] (1) 0/0 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg)
            self.assertEqual(std_out.getvalue(), res)

        rtg2 = Rectangle(1, 2, 3, 4)
        res = "[Rectangle] (2) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg2)
            self.assertEqual(std_out.getvalue(), res)

        rtg3 = Rectangle(5, 12, 4, 7)
        res = "[Rectangle] (3) 4/7 - 5/12\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(rtg3)
            self.assertEqual(std_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as std_out:
            print(r)
            self.assertEqual(std_out.getvalue(), res)

        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as std_out:
            print(type(r.to_dictionary()))
            self.assertEqual(std_out.getvalue(), res)
