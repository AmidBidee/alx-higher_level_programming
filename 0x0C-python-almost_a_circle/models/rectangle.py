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

        self.validate_args(width=width, height=height, x=x, y=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id=id)

    @property
    def width(self):
        """ 
        Return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width
        """
        self.validate_args(width=value)
        self.__width = value

    @property
    def height(self):
        """
        Return height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height
        """
        self.validate_args(height=value)
        self.__height = value

    @property
    def x(self):
        """
        Returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x 
        """
        self.validate_args(x=value)
        self.__x = value

    @property
    def y(self):
        """ 
        Returns y 
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ 
        Sets y 
        """
        self.validate_args(y=value)
        self.__y = value

    def validate_args(self, **kwargs):
        """
        Argument 
        validator
        """
        for arg in kwargs:
            if type(kwargs[arg]) != int:
                raise TypeError(f'{arg} must be an integer')

            if arg in ('width', 'height') and kwargs[arg] <= 0:
                raise ValueError(f'{arg} must be > 0')

            if arg in ('x', 'y') and kwargs[arg] < 0:
                raise ValueError(f'{arg} must be >= 0')
        return True
