#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    dictionary = {}
    for y, value in a_dictionary.items():
        dictionary[y] = value * 2
    return dictionary
