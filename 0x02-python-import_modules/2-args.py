#!/usr/bin/python3

import sys

length = len(sys.argv) - 1

if length == 0:
    print("0 arguments.")

if length == 1:
    print("1 argument:")
    print("1: " + sys.argv[1])

if length > 2:
    print ("{} arguments:".format(length))
    for k in range(1, length + 1):
        st = sys.argv[k]
        print("{}: ".format(k) + st)
