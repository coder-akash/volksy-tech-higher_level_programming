#!/usr/bin/python3
''' task 12 '''


def pascal_triangle(n):
    ''' function '''
    if n <= 0:
        return []
    else:
        lst = []
        for i in range(n):
            l = [int(j) for j in str(11**i)]
            lst.append(l)
        return lst
