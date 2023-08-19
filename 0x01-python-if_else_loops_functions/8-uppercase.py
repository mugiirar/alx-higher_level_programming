#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for p in str:
        if ord(p) >= 97 and ord(p) <= 122:
            p = chr(ord(p) - 32)
        print("{}".format(p), end="")
    print("")

