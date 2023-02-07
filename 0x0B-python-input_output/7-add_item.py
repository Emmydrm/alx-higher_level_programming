#!/usr/bin/python3
"""
This script adds all arguemnts to a python list and then saves them to a file
"""
import json
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


arg_list = []
if __name__ == '__main__':
    for argument in argv:
        # check if it's the first argument
        if argv.index(argument) == 0:
            continue
        # add other arguments to a list
        arg_list.append(argument)

    try:
        # load existing list
        new_list = load_from_json_file("add_item.json")
        # add new list
        new_list += arg_list
        # save newly created list
        save_to_json_file(new_list, "add_item.json")
    except FileNotFoundError:
        # if there's no exissting list create it
        save_to_json_file(arg_list, "add_item.json")
