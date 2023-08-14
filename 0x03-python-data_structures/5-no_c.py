#!/usr/bin/env python3
# 5-no_c.py

def no_c(my_string):
    """Remove all characters c and C from a string."""
    result = ""

    for lett in my_string:
        if lett != 'c' and lett != 'C':
            result += lett

    return result
