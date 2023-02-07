#!/usr/bin/python3
"""This module defines a function 'append_after'"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename: file to be edited
        search_string: string to search for
        new_string: string to be inserted after line containing search_string
    """

    # read file
    file = ""
    with open(filename, encoding='utf-8') as f:
        line = "".join(f.readline())
        while line != "":
            if search_string in line:
                line += new_string
            file += line
            line = "".join(f.readline())
        # write file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(file)
