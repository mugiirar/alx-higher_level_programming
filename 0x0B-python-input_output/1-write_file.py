#!/usr/bin/python3
"""function thar writes to a file"""


def write_file(filename="", text=""):
    """defination of writing to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        written = file.write(text)
        return written
