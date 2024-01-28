#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_by_2 = False
    for i in my_list:
        if i % 2 == 0:
            divisible_by_2 = True
        else:
            divisible_by_2 = False
        i += 1
    return divisible_by_2
