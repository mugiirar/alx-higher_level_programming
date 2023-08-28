#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    k = 0
    while k < x:
        try:
            print(f"{my_list[k]}", end="")
            k = k + 1

        except IndexError:
            break
    print()
    return k
