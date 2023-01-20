#!/usr/bin/python3
''' task 13 '''


def append_after(filename="", search_string="", new_string=""):
    ''' function '''
    x = ""
    with open(filename, encoding='utf_8') as fp:
        for line in fp:
            x += line
            if search_string in line:
                x += new_string
        with open(filename, "w") as fp1:
            fp1.write(x)
