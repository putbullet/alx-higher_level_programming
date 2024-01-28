#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    else:
        M = my_list[0]
        for i in my_list:
            if M < i:
                M = i
        return M
