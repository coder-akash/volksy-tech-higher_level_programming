#!/usr/bin/python3
def safe_print_list(l, x):
    try:
        for i in l[:x]:
            print(i, end='')
        print()
        if len(l) < x:
            return len(l)
        else:
            return x
    except ValueError:
        pass
