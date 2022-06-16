#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''
    Safely prints the integer elements of a list
    Parameters:
    my_list (list): The list containing the elements to be printed
    x (int): The number of elements to print
    Returns:
    The actual number of elements printed
    '''
    n = 0
    for i in range(x):
        item = my_list[i]
        try:
            print("{:d}".format(item), end="")
            n += 1
        except Exception:
            continue
    print("")
    return n
