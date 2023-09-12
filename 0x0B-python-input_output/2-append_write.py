#!/usr/bin/python3
"""append to the end"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        added = file.write(text)
        return added
