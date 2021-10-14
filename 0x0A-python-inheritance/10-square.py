#!/usr/bin/python3
"""
Square method
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square object class"""
    def __init__(self, size):
        """ Constructor """
        super().__init__(size, size)
