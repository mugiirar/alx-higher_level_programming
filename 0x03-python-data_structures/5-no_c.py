#!/usr/bin/env python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [p for p in my_string if p != 'c' and p != 'C']
    return "".join(copy)
