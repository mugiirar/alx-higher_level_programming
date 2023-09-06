#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    k = 0
    while k < size:
        p = 0
        while p < size:
            print("#", end="")
            p += 1
        print("")
        k += 1
