#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    large = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > large:
            large = my_list[i]

    return (large)
