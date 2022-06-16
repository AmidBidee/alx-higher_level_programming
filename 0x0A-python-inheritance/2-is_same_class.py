#!/usr/bin/python3
'''A module for inspecting an object.
'''


def is_same_class(obj, a_class):
    '''Checks if an object is exactly an instance of the specified class.
    Args:
        obj (any): an object to be checked.
        a_class (any): A class to be compared against.
    Returns:
        bool: True if obj is exactly an instance of `a_class`.
    '''
    return type(obj) is a_class
