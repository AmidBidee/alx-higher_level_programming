#!/usr/bin/python3
"""
append_write: function that appends a string
at the end of a text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ appends a string to the end of a text file """
    with open(filename, mode="a", encoding='utf-8') as f:
        f.write(text)
    return len(text)
