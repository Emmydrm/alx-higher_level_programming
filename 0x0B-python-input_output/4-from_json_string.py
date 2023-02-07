#!/usr/bin/python3
"""This module defines a function 'from_json_string'"""
import json


def from_json_string(my_str):
    """returns a python data structure

    Args:
        my_str: JSON string
    """

    return json.loads(my_str)
