#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix is a list of list, div is an int and float"""
    msg_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg_err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMatrix = [[]]
    for mem in matrix:
        if not isinstance(mem, list):
            raise TypeError(msg_err)
        if len(mem) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in mem:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg_err)

    newMatrix = [[round(elem/div, 2) for elem in mem] for mem in matrix]

    return newMatrix
