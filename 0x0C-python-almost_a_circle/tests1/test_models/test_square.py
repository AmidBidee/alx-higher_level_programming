#!/usr/bin/python3
"""
square test module
"""

import unittest
from unittest.mock import patch
from io import StringIO

# models
from models import (Base, Square)


class RectangleTests(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)

    def test_init(self):
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)

    def test_dimensions(self):
        self.assertEqual((self.s1.width, self.s1.height), (5,5))
        self.assertEqual((self.s2.width, self.s2.height), (2,2))
        self.assertEqual((self.s3.width, self.s3.height), (3,3))

    def test_axis(self):
        self.assertEqual((self.s1.x, self.s1.y), (0,0))
        self.assertEqual((self.s2.x, self.s2.y), (2,0))
        self.assertEqual((self.s3.x, self.s3.y), (1,3))

    def test_size_methods(self):
        self.s1.size = 10
        self.s2.size = 5
        
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 5)

    def test_size_validation(self):
        with self.assertRaises(TypeError) as e:
            self.s1.size = '10'
        expection = str(e.exception)
        self.assertEqual(expection, 'width must be an integer')

        with self.assertRaises(TypeError) as e:
            self.s2.size = '5'
        expection = str(e.exception)
        self.assertEqual(expection, 'width must be an integer')

        with self.assertRaises(TypeError) as e:
            self.s3.size = True
        expection = str(e.exception)
        self.assertEqual(expection, 'width must be an integer')

        with self.assertRaises(TypeError) as e:
            self.s1.size = 4.5
        expection = str(e.exception)
        self.assertEqual(expection, 'width must be an integer')


    def tearDown(self):
        Base.reset_objects()
