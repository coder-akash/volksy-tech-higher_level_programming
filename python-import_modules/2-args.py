#!/usr/bin/python3
if __name__ == 'main':
    from sys import argv
    print('{} argument:'.format(len(argv)))
    c=1
    for i in argv:
        print('{}: {}'.format(c, i))
        c += 1
