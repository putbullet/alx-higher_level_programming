#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for list in range(len(my_list)):
        print("{}".format(my_list[list]))
        list += list + 1
