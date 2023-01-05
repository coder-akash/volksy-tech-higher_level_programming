#!/usr/bin/python3
def add_tuple(tup1,tup2):
    if len(tup1) > 2:
        tup1 = tup1[:2]
    elif len(tup1) == 1:
        tup1 = tuple((tup1[0], 0))
    elif len(tup1) == 0:
        tup1 = tuple((0, 0))
    elif len(tup2) > 2:
        tup2 = tup2[:2]    
    elif len(tup2) == 1:
        tup2 = tuple((tup2[0], 0))
    elif len(tup2) == 0:
        tup2 = tuple((0, 0))
    a, b = tup1
    c, d = tup2
    return tuple((a + c, b + d))
