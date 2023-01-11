#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted([key for key in a_dictionary])
    new_dict = {}
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
