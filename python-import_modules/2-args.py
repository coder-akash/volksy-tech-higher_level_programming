#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    print('{} argument:'.format(len(argv)-1))
    for i in range(1, len(argv):
        print('{}: {}'.format(i, argv[i]))
