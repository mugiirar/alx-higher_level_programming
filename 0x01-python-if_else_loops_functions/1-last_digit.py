#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    numb = -1 * number
else:
    numb = number

digit = numb % 10

print("Last digit of", end="")

print(" {} is {}".format(number, digit), end="")

if digit < 5 and digit != 0:
    print(" and is less than 6 and not 0")

if digit == 0:
    print(" and is 0")

if digit > 5:
    print(" and is greater than 5")
