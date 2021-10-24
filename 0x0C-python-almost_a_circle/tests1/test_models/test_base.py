#!/usr/bin/python3
"""
Base test module
"""

import unittest
# model
from models.base import Base


class BaseClasstests(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def test_default_ids(self):
        base2 = Base()
        base3 = Base()
        self.assertEqual(self.base.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_custom_id(self):
        c_base = Base(4)
        self.assertEqual(c_base.id, 4)

    def tearDown(self):
        Base.reset_objects()
