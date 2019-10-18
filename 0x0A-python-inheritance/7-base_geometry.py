#!/usr/bin/python3
"""
BaseGeometry module
"""


class BaseGeometry:
    """
    empty class
    """

    def area(self):
        """raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value"""
#        if not isinstance(value, int):
#        if type(value) is not int:
        if value.__class__ is not int
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
