#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print('0' + '{}'.format(str(i)), end=', ')
    elif i >= 10 and i < 99:
        print('{}'.format(str(i)), end=', ')
    else:
        print('{}'.format(str(i)))
