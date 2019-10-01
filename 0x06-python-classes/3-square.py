#!/usr/bin/python3
"""
Area of a square
"""


class Square:
    """define variables and methods"""

    def __init__(self, size=0):
        """initialize attributes"""
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
            elif not isinstance(size, int):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end='')
            raise Exception
        except ValueError:
            print("size must be >= 0", end='')
            raise Exception

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2
