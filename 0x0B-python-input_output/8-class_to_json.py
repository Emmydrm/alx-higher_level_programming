#!/usr/bin/python3
"""This module defines a function 'class_to_json'"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object

    Args:
        obj: an instance of a class
    """

    return obj.__dict__
