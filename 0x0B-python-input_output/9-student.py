#!/usr/bin/python3
"""This module defines a class 'Student'"""


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

        def to_json(self):
            """Retrieves a dictionary represenation of a Student instance"""

             return self.__dict__
