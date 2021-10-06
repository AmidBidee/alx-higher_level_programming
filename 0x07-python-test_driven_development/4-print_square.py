#!/usr/bin/python3
"""
This module contains

print_square: prints a square with the character # if validate_args returns True
validate_args: validates arguments 
"""


def validate_args(**kwargs):
    """ Validates args """
    for arg in kwargs:
        if type(kwargs[arg]) not in (float, int):
            raise TypeError(f'{arg} must be an integer')
        if type(kwargs[arg]) == float:
            if kwargs[arg] < 0:
                raise TypeError(f'{arg} must be an integer')
        if kwargs[arg] < 0:
            raise ValueError(f'{arg} must be >= 0')

    return True


def print_square(size):
    """ 
    Prints square with the character # if validate_args returns True
    of size = size
    """

    if validate_args(size=size):
        s = int(size)
        for level in range(s):
            print('#' * s)

