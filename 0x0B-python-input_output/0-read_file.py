#!/usr/bin/python3
"""This module defines a function 'read_file'"""


def read_file(filename=""):
    """Reads a file and prints it to stdout

    Args:
        filename: relative path of file to be printed
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
