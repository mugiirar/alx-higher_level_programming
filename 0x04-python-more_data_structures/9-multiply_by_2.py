#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    ""multiply by two""
    p_dir = a_dictionary.copy()
    list_keys = list(p_dir.keys())

    for i in list_keys:
        p_dir[i] *= 2

    return p_dir
