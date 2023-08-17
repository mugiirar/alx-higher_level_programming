#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        a_dictionary.pop(key)
    return a_dictionary
