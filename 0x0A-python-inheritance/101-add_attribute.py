#!/usr/bin/python3
"""
add_attrinute module
"""
def add_attribute(obj, a, v):
    """ add new attribute function """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
