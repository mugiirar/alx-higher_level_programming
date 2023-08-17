#!/usr/bin/python3
# 4-only_diff_elements.py

def only_diff_elements(set_1, set_2):

    diff_set_1 = set()
    diff_set_2 = set()

    for i in set_1:
        if i not in set_2:
            diff_set_1.add(i)
    for i in set_2:
        if i not in set_1:
            diff_set_2.add(i)

    return diff_set_1.union(diff_set_2)
