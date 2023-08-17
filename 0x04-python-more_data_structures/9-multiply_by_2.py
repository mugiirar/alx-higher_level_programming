#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    p_dir = a_dictionary.copy()
    list_keys = list(p_dir.keys())

    for i in list_keys:
        p_dir[i] *= 2

    return p_dir
