#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints all integers in a list

    Args:
         my_list: List of integers
    """

    for element in my_list:
        print("{:d}".format(element))
