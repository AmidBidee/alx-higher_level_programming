#!/usr/bin/python3
"""
BaseGeometry module
"""
class BaseGeometry:
    """ BaseGeometry object class """
    def area(self):
        """ propused area object method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
