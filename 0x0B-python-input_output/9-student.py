#!/usr/bin/python3
"""student class"""


class Student:
    """class defination of stident"""

    def __init__(self, first_name, last_name, age):
        """student att"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
