#!/usr/bin/python3
"""Defination of base class"""
import json
import os


class Base:
    """Body of the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing the constructor
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a list object to python
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """converting list object to json and savig it
        """
        file_name = cls.__name__+".json"

        if list_objs is None:
            with open(file_name, 'w') as file:
                file.write("[]")

        if list_objs is not None:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dictionaries)
                with open(file_name, 'w') as file:
                    file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """making a json list
        """
        if json_string is None:
            return "[]"
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """making a class from a dictionary
        """
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummer = cls(2,4)

            if cls.__name__ == "Square":
                dummer = cls(3)

            dummer.update(**dictionary)

        return dummer

    @classmethod
    def load_from_file(cls):
        """list of classes from a file of JSON
        """
        path = cls.__name__+ ".json"
        if os.path.getsize(path) == 0:
            return "[]"

        if not os.path.exists(path):
            return "[]"

        with open(path, "r") as file:
                instances = file.read()

        list_inst = Base.from_json_string(instances)

        result = [cls.create(**d) for d in list_inst]

        return result


