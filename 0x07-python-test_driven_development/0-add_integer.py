#!/bin/usr/python3
"""
The Module contains a function that adds two numbers after validating

check_input: This validates the inputs and returns true if
             integers else raises a TypeError
add_integer: adds the input after validation is True
"""


def check_input(**kwargs):
    """ Returns true if arguments are either int or float """
    for arg in kwargs:
        if type(kwargs[arg]) not in (int, float):
            raise TypeError(f'{arg} must be an integer')
    return True


def add_integer(a, b=98):
    """
    function that adds to given integers
    """
    if check_input(a=a, b=b):
        return int(a + b)
