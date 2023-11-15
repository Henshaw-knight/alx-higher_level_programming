#!/usr/bin/python3
"""Matrix_divided function Module"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    Args:
        matrix (list): a list of lists of integers or floats
        div (int or float): number by which all elements of matrix
        would be divided
    Raises:
        TypeError: if `matrix` is not a list of lists of numbers
            or if each row of the matrix does not have same size
            or if `div` is not a number (int or float)
        ZeroDivisionError: if `div` is 0
    Return:
        a new matrix with new number lists after division
        and rounding off to 2 decimal places is successful
    """
    new_matrix = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    else:
        length = len(matrix[0])

    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(i/div, 2))

        new_matrix.append(new_row)

    return (new_matrix)
