#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        print('', end='')
    else:
        my_list = reversed(my_list)
        for num in my_list:
            print('{:d}'.format(num))

#    return print('{}'.format(my_list))
