#!/usr/bin/python3
def safe_print_list_integers(l, x):
    try:
        c = 0
        for i in range(x):
            if type(l[i]) == int:
                print('{:d}'.format(l[i]), end="")
                c += 1
        print()
        return c
    except Exception:
        pass
