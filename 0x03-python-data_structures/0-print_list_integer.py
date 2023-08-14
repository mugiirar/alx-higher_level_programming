#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):

    i = 0;

    while i <= (len(my_list) - 1):
        """integers of a list."""
        print("{:d}".format(my_list[i]))
        i += 1
