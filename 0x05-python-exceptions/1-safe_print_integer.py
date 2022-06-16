#!/usr/bin/python3
def safe_print_integer(value):
    ''' Safely prints an integer

    Parameters:
    value (int): The integer to print
    
    Returns:
    True if the integer was successfully printed, otherwise False'''
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
