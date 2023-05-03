#!/usr/bin/python3
"""This module defines a function find_peak that finds the peak of a
list of integers
"""


def find_peak(list_of_integers):
    """Finds the peak of a list of integers"""

    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    list_of_integers.sort()
    return list_of_integers[-1]
