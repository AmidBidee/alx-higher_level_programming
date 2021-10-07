#!/usr/bin/python3
"""
This module contains

is_valid: Returns true if arguments are valid
"""


def is_valid(**kwargs):
    """ Returns true if arguments are valid integers """


    for arg in kwargs:
        if isinstance(kwargs[arg], int) != True:
            raise TypeError(f"{arg} must be an integer")
        if kwargs[arg] < 0:
            raise ValueError(f"{arg} must be >= 0")

    return True


class Rectangle:
    """ Rectangle object """

    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        """ Initialize a Rectangle instance """

        if is_valid(width=width, height=height):
            self.__width = width
            self.__height = height



    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        if is_valid(width=value):
            self.__width = value


    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        if is_valid(height=value):
            self.__height = value



    def area(self):
        """ Returns area of Rectangle """
        return self.__width * self.__height



    def perimeter(self):
        """ Returns perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)



    def __str__(self):
        """ print a string representation of the Rectangle with #"""
        strp = ''
        if self.__width == 0 or self.__height == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                    strp += '#'
            if h < self.__height - 1:
                strp += '\n'

        return strp
