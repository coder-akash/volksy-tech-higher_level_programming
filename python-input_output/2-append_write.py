#!/usr/bin/python3
''' task 2 '''


def append_write(filename="", text=""):
    ''' function '''
    with open(filename, 'a', encoding='utf_8') as fp:
        fp.write(text)
        return len(text)
