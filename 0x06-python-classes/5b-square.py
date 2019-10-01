#!/usr/bin/python3


class Square:

    def __init__(self, size=0):

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

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

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

        return self.__size ** 2

    def my_print(self):

        if self.__size is 0:
            print('')
        for j in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print('')
