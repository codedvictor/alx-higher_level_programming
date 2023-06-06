#!/usr/bin/python
"""
function that divides all elements of a matrix

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
"""

def matrix_divided(matrix, div):
    
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
