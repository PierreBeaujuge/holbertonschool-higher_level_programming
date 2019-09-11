#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print('0' + str(i), end=', ')
    elif i >= 10 and i < 99:
        print(str(i), end=', ')
    else:
        print(str(i))
