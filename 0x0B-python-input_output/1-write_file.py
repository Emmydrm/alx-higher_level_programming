#!/usr/bin/python3
"""This module defines a function 'write_file'"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number
    of characters written

    Args:
        filename: relative path of txt file
        text: text to be written to file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
