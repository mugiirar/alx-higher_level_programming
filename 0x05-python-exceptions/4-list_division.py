#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    track = 0
    length = []
    while track < list_length:
        try:
            element = my_list_1[track] / my_list_2[track]
            
        except ZeroDivisionError:
            element = 0
            print("division by 0")

        except TypeError:
            element = 0
            print("wrong type")

        except IndexError:
            element = 0
            print("out of range")

        finally:
            length.append(element)
            track += 1
    return length
