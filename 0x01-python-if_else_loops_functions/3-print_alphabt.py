#!/usr/bin/python3
n = 97
while (n >= 97 and n <= 122):
    if (n != 101 and n != 113):
        print("{}".format(chr(n)), end="")
    n += 1
