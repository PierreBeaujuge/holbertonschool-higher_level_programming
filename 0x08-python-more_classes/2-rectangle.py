#!/usr/bin/python3
"""
Rectangle management module
"""


class Rectangle:
    """define variables and methods"""

    def __init__(self, width=0, height=0):
        """initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """define area method, evaluate rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """define perimeter method, evaluate rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
