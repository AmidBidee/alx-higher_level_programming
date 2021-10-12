#!/usr/bin/python3
"""
read_file: reads a text file (utf-8) and
            prints to the stdout
"""


def read_file(filename=""):
    """ read and print a text file """
    with open(filename) as file:
        text = file.read()
    print(text)
