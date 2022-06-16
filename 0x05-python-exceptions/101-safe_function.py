#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''
    Safely executes a function
    Parameters:
    fct (function): The function to execute
    args (tuple): The function's arguments
    Returns:
    The result of the function, otherwise None
    '''
    try:
        return fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: ")
        sys.stderr.write(ex.args[0])
        sys.stderr.write("\n")
        return None
