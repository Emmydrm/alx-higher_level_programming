#!/usr/bin/python3
"""This module defines a class 'Student' based on 10-student.py"""


class Student:
    """Defines a student

    Args:
        first_name: first name of student
        last_name: last_name of student
        age: age of student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary represenation of a Student instance

        Args:
            attrs: list of strings to be retrived
        """
        # check attrs is a list of strings
        if type(attrs) != list:
            return self.__dict__
        for string in attrs:
            if type(string) != str:
                return self.__dict__

        # return the specified attributes
        new_dict = {}
        for string in attrs:
            try:
                new_dict[string] = self.__dict__[string]
            except KeyError:
                continue

        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json: dictionary of attributes"""

        for key, value in json.items():
            self.__dict__[key] = value
