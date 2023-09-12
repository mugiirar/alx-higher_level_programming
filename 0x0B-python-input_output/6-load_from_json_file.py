#!/usr/bin/python3
"""creates an object from a file"""


import json


def load_from_json_file(filename):
    """defination of function"""
    with open(filename, 'r', encoding='utf-8') as file:
        return (json.load(file))
