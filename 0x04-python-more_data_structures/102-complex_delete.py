#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []
    
    for kiey, vaal in a_dictionary.items():
        if vaal == value:
            keys_to_delete.append(kiey)
            
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
