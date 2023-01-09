#!/usr/bin/python3
def safe_print_list(l, x):
    try:
        c = 0
        for i in l[:x]:
            print(i, end='')
            c += 1
        print()
        return c
    except:
        pass
