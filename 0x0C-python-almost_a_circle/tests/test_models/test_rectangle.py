"""
rectangle tests
"""

from io import StringIO
import unittest
from unittest.mock import patch

# models
from models.rectangle import Rectangle
from models.base import Base

class RectangleTests(unittest.TestCase):

    def setUp(self):
        self.rec = Rectangle(10, 2, 0, 0)

    def test_init(self):
        self.assertEqual(self.rec.id, 1)

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

    @unittest.skipUnless('area' in dir(Rectangle), 'area not implemented yet')
    def test_area(self):
        self.rec2 = Rectangle(3, 2)
        self.rec3 = Rectangle(2, 10)
        self.rec4 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(self.rec2.area(), 6)
        self.assertEqual(self.rec3.area(), 20)
        self.assertEqual(self.rec4.area(), 56)

    @unittest.skipUnless('display' in dir(Rectangle), 
            'display method not implemented yet')
    def test_display(self):
        rec2 = Rectangle(3, 2)
        rec3 = Rectangle(2, 10)
        rec4 = Rectangle(4, 7, 0, 0, 12)

        with patch('sys.stdout', new=StringIO()) as _stdout:
            rec2.display()
        self.assertEqual(_stdout.getvalue(), "###\n###\n")

        with patch('sys.stdout', new=StringIO()) as _stdout:
            rec3.display()
        self.assertEqual(_stdout.getvalue(), "##\n##\n##\n##\n##\n##\n##\n##\n##\n##\n")

        with patch('sys.stdout', new=StringIO()) as _stdout:
            rec4.display()
        self.assertEqual(_stdout.getvalue(), "####\n####\n####\n####\n####\n####\n####\n")

    @unittest.skipUnless('__str__' in dir(Rectangle), "string method not implemented yet")
    def test_stringmethod(self):
        self.rec6 = Rectangle(4, 6, 2, 1, 12)
        self.rec7 = Rectangle(5, 5, 1, id=13)

        self.assertEqual(str(self.rec6), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(self.rec7), "[Rectangle] (13) 1/0 - 5/5")

    @unittest.skipUnless('display' in dir(Rectangle),
            'display method not implemented yet')
    def test_displaywith_xy(self):
        pass

    @unittest.skipUnless('update' in dir(Rectangle),
            'update method not implemented yet')
    def test_update(self):
        rec8 = Rectangle(4, 6, 2, 1, 12)
        rec9 = Rectangle(5, 5, 1, id=13)

        rec8.update(89, 2, 3, 4, 5)
        rec9.update(90, 5, 4, 0)

        self.assertEqual(str(rec8), '[Rectangle] (89) 4/5 - 2/3')
        self.assertEqual(str(rec9), '[Rectangle] (90) 0/0 - 5/4')

    @unittest.skipUnless('update' in dir(Rectangle),
            'update method not implemented yet') 
    def test_update_kwargs(self):
        rec10 = Rectangle(4, 6, 2, 1, 12)
        rec11 = Rectangle(5, 5, 1, id=13)

        with self.assertRaises(TypeError) as e:
            rec10.update('5', height='7', x='0')
        exception = str(e.exception)
        self.assertEqual(exception, 'id must be an integer')

        with self.assertRaises(TypeError) as e:
            rec11.update(6, height='7', x='0')
        exception = str(e.exception)
        self.assertEqual(exception, 'height must be an integer')

        rec11.update(x=1, height=3)
        rec10.update(y=1, width=6, x=3, id=100)

        self.assertEqual(str(rec10), '[Rectangle] (100) 3/1 - 6/6')
        self.assertEqual(str(rec11), '[Rectangle] (6) 1/0 - 5/3')

    def test_doc(self):
        self.assertEqual(type(Rectangle.__doc__), str)

    def tearDown(self):
        Base.reset_objects()
        del(self.rec)
