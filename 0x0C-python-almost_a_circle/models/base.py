#!/usr/bin/python3
"""
This module represents the base class for all
subsequent classes in this package
"""

import json


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_objects():
        """
        Resets number of objects for testing
        """
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            if type(list_dictionaries) != list:
                raise TypeError("list_dictionaries must be a list")
            json_dictionaries = json.dumps(list_dictionaries)
            return json_dictionaries
        return '[]'

    def save_to_file(cls, list_objs):
        if list_objs != None:
            j_string = cls.to_json_string(list_objs)
        else:
            j_string = []
        
        f_name = cls.__name__
        with open(f'{name}.json', 'w') as f:
            json.dump(j_string, f)
