#!/usr/bin/python3
def safe_print_list_integers(l, x):
    try:
        c = 0
        for i in l[:x]:
            if type(i) == int:
                print('{:d}'.format(i), end="")
                c += 1
        print()
        return c
    except (ValueError, IndexError):
        pass
