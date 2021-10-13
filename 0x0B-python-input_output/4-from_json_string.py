#!/usr/bin/python3
"""
from_json_string: function that returns an object
(Python data structure) represented by a JSON string
"""

import json


def def from_json_string(my_str):
    """ Return object representation by a JSON string """
    return json.loads(my_str)
