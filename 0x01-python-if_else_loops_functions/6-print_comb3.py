#!/usr/bin/python3

for number in range(0, 10):
    for value in range (number + 1, 10):
        print("{}{}".format(number, value), end=", " if number < 8 or value < 9 else "\n")
