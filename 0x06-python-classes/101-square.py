#!/usr/bin/python3


class Square:

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

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

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):

        try:
            if isinstance(value, tuple) and len(value) is 2 and value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers", end='')
            raise Exception


    def area(self):

        return self.__size ** 2

    def my_print(self):

        if self.__size is 0:
            print('')
        if self.__position[1] > 0:
            for k in range(self.__position[1]):
                print('')
        for j in range(self.__size):
            if self.__position[0] > 0:
                for l in range(self.__position[0]):
                    print(' ', end='')
            for i in range(self.__size):
                print('#', end='')
            print('')
