#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    position = 0
    k = 0
    while position < x:
        try:
            print("{:d}".format(my_list[position]), end="")
            position += 1
            k += 1
        except (ValueError, TypeError):
            position += 1
            continue

    print()
    return k
