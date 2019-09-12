#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    argc = len(sys.argv)
    result = 0
    if argc > 1:
        for arg in sys.argv[1:]:
            result += int(arg)
    print('{:d}'.format(result))
