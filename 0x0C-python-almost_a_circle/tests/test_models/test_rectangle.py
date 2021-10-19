#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib


class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""

    def test_Rectangleinheritance(self):
        """This function tests that rectangle inherits from Base"""
        Rectangle.reset_objects()
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_objectinheritance(self):
        """This function tests that rectangle inherits from Base"""
        Rectangle.reset_objects()
        r1 = Rectangle(1, 1)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_errorfornoarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: 'width' and" +
            " 'height'")

    def test_errorfor1argument(self):
        """This function tests that Typeerror is thrown when 1 argument"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1)
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'height'")

    def test_errorfortoomanyarguments(self):
        """This function tests that Valueerror is thrown when extra args"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, 4, 5, 7)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional arguments but 7 were given")
