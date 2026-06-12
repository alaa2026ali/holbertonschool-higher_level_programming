#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor (div).

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int/float): The number to divide the matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with results rounded to 2 decimal places.
    """
    # 1. Check if matrix is a list of lists containing only integers or floats
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)
    
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    # 2. Check if all rows have the same size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # 3. Check if div is a valid number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Perform the division and round to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]
