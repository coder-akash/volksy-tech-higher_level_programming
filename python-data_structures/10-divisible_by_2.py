#!/usr/bin/python3
def divisible_by_2(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return new_lst
