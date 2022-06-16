#!/usr/bin/python3
def weight_average(my_list=[]):
    '''
    Computes the weighted average of all integers tuple (<score>, <weight>)
    Parameters:
    my_list (list): A list of 2-tuples in the form (<score>, <weight>)
    Returns:
    The weigthed average
    '''
    if (not isinstance(my_list, list)) or len(my_list) == 0:
        return 0
    dx = sum(map(lambda item: item[0] * item[1], my_list))
    dy = sum(map(lambda item: item[1], my_list))
    return dx / dy
