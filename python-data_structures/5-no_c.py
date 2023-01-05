#!/usr/bin/python3
def no_c(st):
    new_st = ''
    for i in st:
        if i != 'c' and i != 'C':
            new_st = new_st + i
    return new_st
