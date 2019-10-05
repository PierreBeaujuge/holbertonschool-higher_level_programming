#!/usr/bin/python3
"""
Module that handles
the division of
matrix elements
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if not (isinstance(matrix, list) and len(matrix) > 0):
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    for element in matrix:
        if not (isinstance(element, list) and len(element) > 0):
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        for num in element:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
    i = 0
    for i in range(len(matrix) - 1):
        i += 1
        if len(matrix) > 1 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda num: round(num / div, 2),
                     element)) for element in matrix]
