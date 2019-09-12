#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    argc = len(sys.argv)
    if argc == 1:
        print('{:d} arguments.'.format(argc - 1))
    elif argc == 2:
        print('{:d} argument:\n'.format(argc - 1) + '{:d}: {}'.format(sys.argv.index(sys.argv[1]), sys.argv[1]))
    else:
        print('{:d} arguments:'.format(argc - 1))
        for arg in sys.argv[1:]:
            print('{:d}: {}'.format(sys.argv.index(arg), arg))
