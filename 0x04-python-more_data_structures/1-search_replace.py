#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):    
    new_list = list(my_list)
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list