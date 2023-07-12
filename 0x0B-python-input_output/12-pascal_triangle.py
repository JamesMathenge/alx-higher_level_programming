#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
        Each inner list represents a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i-1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
