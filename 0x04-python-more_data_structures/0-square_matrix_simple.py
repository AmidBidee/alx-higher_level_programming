#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m_copy = matrix.copy()
    m_copy = [[(i[n]**2) for n in range(3)] for i in m_copy]
    return m_copy
