#!/usr/bin/python3
''' task 1 '''


def write_file(filename="", text=""):
    ''' function '''
    with open(filename, 'w', encoding='utf_8') as fp:
        fp.write(text)
        return len(text)
