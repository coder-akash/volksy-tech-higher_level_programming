#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    lst = list(int(x) for x in argv[1:])
    print(sum(lst))
