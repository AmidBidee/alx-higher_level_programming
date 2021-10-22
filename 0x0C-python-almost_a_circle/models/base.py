#!/usr/bin/python3
"""
This module represents the base class for all
subsequent classes in this package
"""


class Base:
    """
    Base class
    Attributes:
     __nb_objects: this is for the object id and number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiate a new Base class
            Args:
                id: is used to manage objects
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    def reset_objects():
        """
        Resets number of objects for testing
        """
        Base.__nb_objects = 0
