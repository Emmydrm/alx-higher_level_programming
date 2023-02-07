#!/usr/bin/python3
"""This module defines a function 'append_write'"""


def append_write(filename="", text=""):
    """Appends a text to a file

    Args:
        filename: relative path of file
        text: text to be written
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
