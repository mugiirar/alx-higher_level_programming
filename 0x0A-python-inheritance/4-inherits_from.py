#!/usr/bin/python3
"""check  if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """defiination of the function"""
    if isinstance(obj, a_class) and obj.__class__ != a_class:
        return True
    return False
