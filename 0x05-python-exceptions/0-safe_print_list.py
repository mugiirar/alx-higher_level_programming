#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    
    k = 0

    while k <= x:
        try:
            print("", my_list[k], end="")
            k = k + 1

        except IndexError:
            break

    print("")

    return k
