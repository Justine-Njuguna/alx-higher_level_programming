#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number"""

    if not isinstance(matrix, list) or not \
    all(isinstance(row, list) for row in matrix):
        """Raise TypeError where matrix must be a matrix of ints or floats"""

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        """Raise TypeError where matrix must be a matrix of ints or floats"""

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        """Raise TypeError where matrix must be a matrix of ints or floats"""

        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        """Raise TypeError where div must be a number"""

        raise TypeError("div must be a number")

    if div == 0:
        """Raise ZeroDivisionError that forbids division by 0"""

        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
