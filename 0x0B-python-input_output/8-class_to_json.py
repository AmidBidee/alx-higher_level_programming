#!/usr/bin/python3
"""
class_to_json: function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """ Returns dictionary description with simple data structure of obj """
    return obj.__dict__
