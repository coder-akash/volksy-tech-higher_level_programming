#!/usr/bin/python3
''' task 13 '''


def append_after(filename="", search_string="", new_string=""):
    ''' function '''
    with open(filename, encoding='utf_8') as fp:
        x = fp.readlines()
        for i in x:
            if search_string in i:
                x.insert(x.index(i)+1, new_string)
        with open(filename, 'w', encoding='utf_8') as fp1:
            fp1.writelines(x)
