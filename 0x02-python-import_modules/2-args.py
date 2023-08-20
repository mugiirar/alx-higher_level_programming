#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length))

    if length == 1:
        print("{} argument:".format(length))
        print("{}: ".format(length) + sys.argv[1])

    if length > 2:
        print ("{} arguments:".format(length))
        for k in range(1, length + 1):
            st = sys.argv[k]
            print("{}: ".format(k) + st)
