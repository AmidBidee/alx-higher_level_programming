#!/usr/bin/python3
"""
MyInt module
"""
class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """ equal to operator """
        return self - other != 0

    def __ne__(self, other):
        """ not equal to operator """
        return self - other == 0
