#!/usr/bin/python3
"""sorting a list"""


class MyList(list):
    """defination of the function"""
    def print_sorted(self):
        """sorts the list"""
        print(sorted(self))
