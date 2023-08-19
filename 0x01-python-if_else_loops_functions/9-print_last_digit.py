#!/usr/bin/env python3
# 9-print_last_digit.py

def print_last_digit(number):

    if number < 0:
        number = -1 * number
    k = number % 10

    print("{}".format(k), end="")

    return (k)
