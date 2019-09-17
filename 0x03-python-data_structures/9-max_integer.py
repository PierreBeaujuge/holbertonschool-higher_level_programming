#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    for num in my_list:
        for i in range(my_list.index(num) + 1, len(my_list)):
            if num < my_list[i]:
                break
            if i == len(my_list) - 1:
                return num
            else:
                continue
    return num
