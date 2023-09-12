#!/usr/bin/python3
"""append to the end"""


def append_write(filename="", text=""):
    """appemding to file"""
    with open(filename, "a", encoding="utf-8") as file:
        added = file.write(text)
        return added
