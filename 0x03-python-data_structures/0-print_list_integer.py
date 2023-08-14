#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """integers of a list."""

    i = 0;
    k = len(my_list) - 1;

    while i <= k:
        print("{:d}".format(my_list[i]))
        i += 1
