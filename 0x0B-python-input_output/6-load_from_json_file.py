#!/usr/bin/python3
"""
load_from_json_file: function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """ creates an object from json file """
    with open(filename, 'utf-8') as file:
        return json.load(file)
