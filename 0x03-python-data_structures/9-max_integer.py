#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    else:
        M = my_list[0]
        for i in my_list:
            if M < my_list[i]:
                M = my_list[i]
                return M
            else:
                return M
