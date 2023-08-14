#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list."""

    new_list = my_list[:]

    if idx < 0 or idx >= len(new_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list
