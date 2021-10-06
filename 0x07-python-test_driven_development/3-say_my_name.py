"""
This module contains

say_my_name: prints My name is <first name> <last name
validate_args: checks and validates arguments,
                raises Exceptions if encountered
"""


def validate_args(**kwargs):
    """ Returns true if args are strings else raises TypeError """

    for arg in kwargs:
        if type(kwargs[arg]) != str:
            raise TypeError(f'{arg} must be a string')

    return True


def say_my_name(first_name, last_name=""):
    if validate_args(first_name=first_name, last_name=last_name):
        print(f"My name is {first_name} {last_name}")
