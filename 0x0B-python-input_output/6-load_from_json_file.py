#!/usr/bin/python3
"""This module defines a function 'load_from_json_file'"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file

    Args:
        filename: json file

    Returns:
        python object
    """

    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
