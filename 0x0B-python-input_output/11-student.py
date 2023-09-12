#!/usr/bin/python3
"""defination of a student"""


class Student:
    """representation of student"""

    def __init__(self, first_name, last_name, age):
        """initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        return {k: getattr(self, k) for k in attrs if isinstance(k, str) and hasattr(self, k)}

    def reload_from_json(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, value)
