"""
rectangle tests
"""

import unittest
# models
from models.rectangle import Rectangle
from models.base import Base

class RectangleTests(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(10, 2, 0, 0)

    def test_init(self):
        self.assertEqual(self.rec.id, 4)

    def test_dimension(self):
        self.assertEqual((self.rec.width, self.rec.height), (10, 2))

    def test_axis(self):
        self.assertEqual((self.rec.x, self.rec.y), (0, 0))

    def test_validations(self):
        self.assertTrue(Rectangle.validate_args(self.rec, width=15, height=10, x=0, y=15))
        with self.assertRaises(TypeError) as e:
            Rectangle.validate_args(
                    self.rec,
                    width='15',
                    height='10',
                    y=15.5, 
                    x=14.5
                    )
        exception = str(e.exception)
        self.assertEqual(exception, 'width must be an integer')

        with self.assertRaises(ValueError) as e:
            self.rec.validate_args(
                    width=15, 
                    height=-10, 
                    x='0',
                    y='15'
                    )
        exception = str(e.exception)
        self.assertEqual(exception, 'height must be > 0')

        with self.assertRaises(TypeError) as e:
            Rectangle.validate_args(self.rec, width=10, height=5.5)
        exception = str(e.exception)
        self.assertEqual(exception, 'height must be an integer')

        with self.assertRaises(TypeError) as e:
                self.rec.width = '45'
        exception = str(e.exception)
        self.assertEqual(exception, 'width must be an integer')

        with self.assertRaises(TypeError) as e:
                self.rec.height = False
        exception = str(e.exception)
        self.assertEqual(exception, 'height must be an integer')

        with self.assertRaises(TypeError) as e:
                self.rec.x = True
        exception = str(e.exception)
        self.assertEqual(exception, 'x must be an integer')

        with self.assertRaises(TypeError) as e:
                self.rec.y = '0'
        exception = str(e.exception)
        self.assertEqual(exception, 'y must be an integer')

        with self.assertRaises(ValueError) as e:
                self.rec.width = 0
        exception = str(e.exception)
        self.assertEqual(exception, 'width must be > 0')

        with self.assertRaises(ValueError) as e:
                self.rec.x = -10
        exception = str(e.exception)
        self.assertEqual(exception, 'x must be >= 0')

    def test_dimension_setters(self):
        self.rec.width = 15
        self.rec.height = 10
        self.assertEqual((self.rec.width, self.rec.height), (15, 10))

    def tearDown(self):
        Rectangle.id = 0
        del(self.rec)
