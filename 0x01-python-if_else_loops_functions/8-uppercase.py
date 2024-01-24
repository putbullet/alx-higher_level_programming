#!/usr/bin/python3
def uppercase(str):
    result = ""

    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)

    print("{}".format(result))
