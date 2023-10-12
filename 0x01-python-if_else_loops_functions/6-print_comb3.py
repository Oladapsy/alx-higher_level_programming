#!/usr/bin/python3
for firstdigit in range(0, 10):
    for seconddigit in range(firstdigit + 1, 10):
        if firstdigit == 8 and seconddigit == 9:
            print('{}{}'.format(firstdigit, seconddigit)
        else:
            print('{}{}, '.format(firstdigit, seconddigit), end='')
