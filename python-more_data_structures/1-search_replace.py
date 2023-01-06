#!/usr/bin/python3
def search_replace(my_list, s, r):
    lst = list(map(lambda i: r if (i == s) else i, my_list))
    return lst
