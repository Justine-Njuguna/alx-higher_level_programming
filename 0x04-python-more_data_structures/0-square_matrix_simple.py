#!/usr/bin/python3

def square_matrix_simple(matrix):
    if not matrix:
        return []

    result = [[number ** 2 for number in row] for row in matrix]

    return result
