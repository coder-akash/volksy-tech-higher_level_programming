#!/usr/bin/python3
''' task 0 '''


def read_file(filename=""):
    ''' function '''
    with open(filename, encoding='utf_8') as fp:
        print(fp.read()[:-1])
