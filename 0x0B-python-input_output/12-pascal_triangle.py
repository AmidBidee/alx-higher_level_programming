#!/usr/bin/python3
"""
pascal's triangle module

pascal_triangle:
returns a list of lists of integers representing
the Pascal’s triangle of n
    1. if n is greater than 0
        -> start a loop that creates a list while n is greater than 0
        -> each list depends on the previous
        -> each elementof each nth list should follow the order;
            > iterate through the previous if it exists;
            > append the first (this should be 1) element of the previous
                list to the curreny list
            > jump to the next element of the previous list;
            > add the the next(current) element of to the previous element;
            > append it to the list
            > if the next(current) element is the last element
                of the previous list;
            > append it to the end of the current list (this should be 1)
        -> stop when n = 0 then return the list of list
    2. else return an empty list
"""


def pascal_triangle(n):
    """ Returns pascal's triangle """
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        row = []
        if i <= 1:
            for c in range(i+1):
                row.append(1)

        else:
            previous = pascal[len(pascal) - 1]

            c_i = 0
            row.append(previous[0])
            last_elem = len(previous) - 1
            for elem in previous:
                if c_i != 0:
                    e = elem + previous[c_i - 1]
                    row.append(e)
                if c_i == last_elem:
                    row.append(elem)
                c_i += 1

        pascal.append(row)
    return pascal
