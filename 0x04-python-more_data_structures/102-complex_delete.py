#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''
    Deletes keys with a specific value in a dictionary
    Parameters:
    a_dictionary (dict): The dictionary to modify
    '''
    keys = set(a_dictionary.keys())
    for key in keys:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
