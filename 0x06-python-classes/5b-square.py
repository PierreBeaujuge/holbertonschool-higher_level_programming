#!/usr/bin/python3
"""
Printing a square
"""


class Square:
    """define variables and methods"""
    def __init__(self, size=0):
        """initialize attributes"""
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        try:
            if isinstance(value, int) and value >= 0:
                self.__size = value
            elif not isinstance(value, int):
                raise TypeError
            elif value < 0:
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

    def my_print(self):
        """define my_print method, printing of a square"""
        if self.__size is 0:
            print('')
        for j in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print('')
