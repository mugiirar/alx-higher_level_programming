#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except  (ZeroDivisionError,  FloatingPointError):
        result = None
    finally:
        if result != None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
        return result
