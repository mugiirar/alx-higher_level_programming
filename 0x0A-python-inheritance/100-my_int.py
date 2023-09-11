#!/usr/bin/python3
"""inheriting int"""


class MyInt(int):
    """class body"""
    def __eq__(self, value):
        """override"""
        return self.real != value

    def __ne__(self, value):
        """overide"""
        return self.real == value
