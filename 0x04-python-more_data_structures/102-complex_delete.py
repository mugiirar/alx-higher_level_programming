#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    st_keys = list(a_dictionary.keys())

    for value_c in st_keys:
        if value == a_dictionary.get(value_c):
            del a_dictionary[value_c]

    return (a_dictionary)
