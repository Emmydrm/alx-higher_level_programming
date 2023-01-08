#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints a list of integers in reverse order

    Args:
        my_list: list of integers
    """
    if my_list:
        for idx in my_list[::-1]:
            print("{:d}".format(idx))
