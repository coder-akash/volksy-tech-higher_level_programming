#!/usr/bin/python3
def print_reversed_list_integer(a):
    if a is not None:
        for i in a[::-1]:
            print('{:d}'.format(i))
