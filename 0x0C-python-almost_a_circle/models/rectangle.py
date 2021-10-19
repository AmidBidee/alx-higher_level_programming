#!/usr/bin/python3
"""
Rectangle module
"""

from .base import Base


class Rectangle(Base):
    """ Rectangle class """
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id=id)

    @property
    def width(self):
        """ Return width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width """
        self.__width = value

    @property
    def height(self):
        """ Return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        self.__height = value

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x """
        self.__x = value

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y """
        self.__y = value

    def validate(self, prop, val):
        """
        This is a helper class for validating
         inputs to private instance attributes
        """

        if(type(val) is not int):
            raise TypeError('{} must be an integer'.format(prop))
        if (prop in ['x', 'y'] and val < 0):
            raise ValueError('{} must be >= 0'.format(prop))
        elif (prop in ['height', 'width'] and val <= 0):
            raise ValueError('{} must be > 0'.format(prop))
        return val
