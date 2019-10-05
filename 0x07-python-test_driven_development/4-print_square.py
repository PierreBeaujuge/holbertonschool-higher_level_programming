#!/usr/bin/python3
"""
Module that handles
printing
a square
"""


def print_square(size):
    """
    Function that prints a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print('#', end='')
        print('')
