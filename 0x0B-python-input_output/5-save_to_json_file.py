#!/usr/bin/python3
"""This module defines a function 'save_to_json_file'"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file

    Args:
        my_obj: python data structure
        filename: file to be written to
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
