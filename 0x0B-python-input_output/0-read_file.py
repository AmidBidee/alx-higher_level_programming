#!/usr/bin/python3
"""
read_file: reads a text file (utf-8) and
            prints to the stdout
"""


def read_file(filename=""):
    """ read and print a text file """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
