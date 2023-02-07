#!/usr/bin/python3
"""This module defines a function 'to_json_string'"""
import json


def to_json_string(my_obj):
    """Returns the JSON represenation of an object

    Args:
        my_obj: a string
    """

    return json.dumps(my_obj)
