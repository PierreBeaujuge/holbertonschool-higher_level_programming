#!/usr/bin/python3
"""
Module that handles
the addition of
two integers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if (isinstance(a, int) or isinstance(a, float)) and\
       (isinstance(b, float) or isinstance(b, int)):
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a + b
    elif not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
