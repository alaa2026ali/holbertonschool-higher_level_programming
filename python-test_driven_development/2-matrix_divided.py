#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given number, rounding the results to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by `div`.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not of equal size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix containing the divided values rounded to 2 decimal places.
    """
    # 1. Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Check if div is NaN (Not a Number)
    if div != div:
        raise TypeError("div must be a number")

    # 3. Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 4. Validate matrix structure and elements
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Get the size of the first row to compare with others
    if not isinstance(matrix[0], list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            # Check if elements are int/float and not NaN/Inf
            if not isinstance(element, (int, float)) or element != element:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )
            if element == float("inf") or element == float("-inf"):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )

            # Perform division and round to 2 decimal places
            # Note: Division by float('inf') will safely result in 0.0
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
