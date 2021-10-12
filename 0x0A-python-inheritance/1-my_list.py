#!/usr/bin/python3
""" This module holds MyList object """


class MyList(list):
    """ MyList object class """
    def print_sorted(self):
        """ A function that sorts and prints the inherited list """
        print(sorted(self))
