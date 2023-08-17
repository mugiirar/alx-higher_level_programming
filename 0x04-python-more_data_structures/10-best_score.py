#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):

    if a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    value = list(a_dictionary.values())

    max_value = max(value)

    index = value.index(max_value)

    return keys[index]
