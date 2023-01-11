#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = dict(a_dictionary)
    for key, val in copy.items():
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
