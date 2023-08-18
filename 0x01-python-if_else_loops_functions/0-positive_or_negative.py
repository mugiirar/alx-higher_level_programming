#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number < 0:
    print(str(number) + " is negative")

if number > 0:
    print(str(number) + " is positive")

if number == 0:
    print(str(number) + " is zero")
