#!/usr/bin/python3
"""
A function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides the integer/float numbers of a matrix
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elements of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    k = 0

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        if k != 0 and len(i) != k:
            raise TypeError("Each row of the matrix must have the same size")

        for num in i:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

        k = len(i)

    p = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (p)
