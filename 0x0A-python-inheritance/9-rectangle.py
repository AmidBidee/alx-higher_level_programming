#!/usr/bin/python3
"""
Rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle object class """
    def __init__(self, width, height):
        """ Instantiate object instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area method """
        return self.__width * self.__height

    def __str__(self):
        """ object string method """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
