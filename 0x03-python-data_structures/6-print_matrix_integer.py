#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for outer in range(len(matrix)):
        m_len = len(matrix[outer])
        for inner in matrix[outer]:
            if matrix[outer].index(inner) != (m_len - 1):
                print("{}".format(inner), end=' ')
            else:
                print("{}".format(inner), end='')
        print()
