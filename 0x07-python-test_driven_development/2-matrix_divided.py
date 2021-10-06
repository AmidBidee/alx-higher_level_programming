"""
This module contains

matrix_divided: divides all elements of a matrix by a given value
                if validate_args returns True
validate_args: Validates arguments returns True if arguments pass
                validation else raises exceptions
_deepcopy: returns a deepcopy of a matrix
"""


def _deepcopy(m):
    """ deepcopy a matrix """

    mc = []
    for row in m:
        if type(row) != list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        mc.append(row.copy())

    return mc


def validate_args(m_copy, **kwargs):
    """
    Validates arguments[matrix, div] and returns True if
    validation requirements are met

    Raises TypeError if  matrix is not (list of lists) and if
    matrix is nor (list of lists) of  ints/floats

    Raises TypeError if row of matrix isnt the same size

    Raises TypeError if div is not a number
    """

    size = len(m_copy[0])
    if size == 0:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')

    for row in m_copy:
        if len(row) != size:
            raise TypeError('Each row of the matrix must have the same size')

    for row in m_copy:
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(
                 'matrix must be a matrix (list of lists) of integers/floats')

    if type(kwargs['div']) not in (int, float):
        raise TypeError('div must be a number')
    if kwargs['div'] == 0:
        raise ZeroDivisionError('division by zero')

    return True


def matrix_divided(matrix, div):
    """ divides all elements of a matrix """

    m_copy = [[]]
    if m_copy and matrix:
        m_copy = _deepcopy(matrix)
    else:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')

    if validate_args(m_copy, div=div):
        for row in m_copy:
            i = 0
            for elem in row:
                m_copy[m_copy.index(row)][i] = round(elem/div, 2)
                i += 1

    return m_copy
