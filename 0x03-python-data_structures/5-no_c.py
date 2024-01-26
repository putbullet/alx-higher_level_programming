#!/usr/bin/python3
def no_c(my_string):
    output = ""
    for char in my_string:
        if char.lower() != "c":
            output += char
    return output
