#!/usr/bin/python3

if __name__ == '__main__':

    import hidden_4

    def vdir(object):
        return [x for x in dir(object) if not x.startswith('__')]

#    print(vdir(hidden_4))

    for x in vdir(hidden_4):
        print('{}'.format(x))
