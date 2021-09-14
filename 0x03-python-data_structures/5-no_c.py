#!/usr/bin/python3
def l_to_str(l=[]):
    temp = ''
    for letter in l:
        temp += letter
    return temp

def no_c(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i].lower() == 'c':
            my_string[i] = ''
    my_string = l_to_str(my_string)
    return my_string

