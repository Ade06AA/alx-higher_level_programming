#!/usr/bin/python3
"""
Module doc
"""

def matrix_divided(matrix, div):
    """
    func that divides all elements of a matrix
    """
    new_matrix = []
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    try:
        size = len(matrix[0])
    except Exception:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for number in i:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            initial = float(number / div)
            result = float("{:.2f}".format(initial))
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
