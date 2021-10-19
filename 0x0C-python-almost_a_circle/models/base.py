#!/usr/bin/python3
"""
Base Module
"""


class Base:
    """ Base class object """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    def reset_objects():
        """Resets number of objects for testing"""
        Base.__nb_objects = 0
