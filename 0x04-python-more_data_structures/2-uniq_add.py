#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    unique_integers = set()
    
    for num in my_list:
        if num not in unique_integers:
            unique_integers.add(num)
    
    return sum(unique_integers)

