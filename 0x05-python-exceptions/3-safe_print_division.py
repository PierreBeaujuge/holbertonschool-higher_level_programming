#!/usr/bin/python3


def safe_print_division(a, b):

    try:
        if a and b:
            result = a / b
        else:
            result = None
    except ZeroDivisionError:
        result = None
    finally:
        print ("Inside result: {}".format(result))
