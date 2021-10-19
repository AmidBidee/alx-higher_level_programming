#!/usr/bin/python3
"""
This module contains

text_indentation: prints a text with 2 new lines
                  after each of these characters: ., ? and :
validate_args: validates args
"""


def validate_args(**kwargs):
    """ Validate arguments """
    for arg in kwargs:
        if type(kwargs[arg]) != str:
            raise TypeError("Something")

    return True


def text_indentation(text):
    """
    prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if validate_args(text=text):
        str_len = len(text)
        for i in range(str_len):
            print(text[i], end="")
            if text[i] in ('.', '?', ':'):
                print('\n')
    print()
