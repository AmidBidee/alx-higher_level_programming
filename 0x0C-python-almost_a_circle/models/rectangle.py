#!/usr/bin/python3
"""
Rectangle module

class: Rectangle
    __init__(widget, height, x=0, y=0)

methods:

    Rectangle.validate_args(self, **kwargs)

    Rectangle.width(self, value)

    Rectangle.height(self, value)
    
"""

from .base import Base


class Rectangle(Base):
    """ 
    Rectangle object class, inherits from the from base.Base class
    creates a Rectangle object instance with a width and height

    attributes:  
        private -->  __width, __height, __x, __y

    Methods:
        validate_args(self, *kwargs):
                validates the arguments passed in, returns true if
                all requirements are passed and raises an exception if not
    """
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor

        Rectangle.__init__(self, width, height x=0, y=0)
            instatiate a Rectangle object with a width and height
        """

        self.validate_args(width=width, height=height, x=x, y=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id=id)

    @property
    def width(self):
        """
        Retrieves the value of the private instance attribute [__width]
        and returns it
        attr: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        assigns value to the private instance attribute [__width]
        if value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(width=value)
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the private instance attribute [__height]
        and returns it
        attr: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        assigns the value to the private instance attribute [__height]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(height=value)
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the value of the private instance attribute [__x]
        and returns it
        attr: self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        assigns the value to the private instance attribute [__x]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(x=value)
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the value of the private instance attribute [__y]
        and returns it
        attr: self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        ssigns the value to the private instance attribute [__y]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(y=value)
        self.__y = value

    def validate_args(self, **kwargs):
        """
        public instance method -->
        validate_args(self, *kwargs):
                validates the arguments passed in, returns true if
                all requirements are passed and raises an exception if not
        """
        for arg in kwargs:
            if type(kwargs[arg]) != int:
                raise TypeError(f'{arg} must be an integer')

            if arg in ('width', 'height') and kwargs[arg] <= 0:
                raise ValueError(f'{arg} must be > 0')

            if arg in ('x', 'y') and kwargs[arg] < 0:
                raise ValueError(f'{arg} must be >= 0')
        return True
