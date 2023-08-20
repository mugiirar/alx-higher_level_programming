#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)

    if length == 1:
        print("{}".format(0))

    k = 0

    if length > 1:
        for p in range(1, length):
            k += int(sys.argv[p])
        print("{}".format(k))
