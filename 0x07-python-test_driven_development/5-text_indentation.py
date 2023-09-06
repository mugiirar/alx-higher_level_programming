#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    k = 0
    p = len(text)
    while k < p:
        print(text[k], end="")
        if text[k] == '.':
            k = k + 1
            print("")
            print("")

        if text[k] == '?':
            k += 1
            print("")
            print("")

        if text[k] == ':':
            k += 1
            print("")
            print("")

        k += 1
