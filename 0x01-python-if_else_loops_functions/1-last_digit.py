#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = str(number)

dig = int(num[-1:])

if dig > 5:
    print("Last digit of "+ num + " is " + num[-1:]+ " and is greater than 5")

if dig == 0:
    print("Last digit of "+ num + " is " + num[-1:]+ " and is greater than 0")

if dig < 6:
    print("Last digit of " + num + " is " + num[-1:] + " and is less than 6 and not 0")
