#!/usr/bin/python3


def uppercase(str):
    for char in str[0:-1]:
        if char >= 'a' and char < '{':
            char = chr(ord(char) - 32)
        print('{}'.format(char), end='')
    if str[-1] >= 'a' and str[-1] < '{':
        char = chr(ord(str[-1]) - 32)
    print('{}'.format(char))
