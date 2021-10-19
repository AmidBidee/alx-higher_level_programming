#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
#from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""
    def test_singleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_multipleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_instancecreationwithid(self):
        """This function tests for 1 instance creation with id"""
        Base.reset_objects()
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_instancecreationwithstringid(self):
        """This function tests for one instance creation with id"""
        Base.reset_objects()
        b1 = Base("foo")
        self.assertEqual(b1.id, "foo")
