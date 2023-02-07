#!/usr/bin/python3
"""This module defines a function 'pascal_triangle'"""


def pascal_triangle(n):
    """Returns a list of lists of numbers

    Args:
        n: number
    """

    triangle = []

    if n <= 0:
        return triangle

    # build triangle
    for i in range(n):
        # build first list
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            new_list = [1]
            # create new list from previous list
            j = 0
            while j < (len(triangle[i - 1]) - 1):
                value = triangle[i - 1][j] + triangle[i - 1][j + 1]
                new_list.append(value)
                j += 1
            new_list.append(1)

            # add new list to triangle
            triangle.append(new_list)

    return triangle
