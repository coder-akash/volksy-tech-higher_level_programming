#!/usr/bin/python3
def safe_print_list_integers(l, x):
    try:
        c = 0
        l.index(x)
        for i in l[:x]:
            if type(i) == int:
                print('{:d}'.format(i), end="")
                c += 1
        print()
        return c
    except IndexError as err:
        return err
