#!/usr/bin/python3
''' task 12 '''


def pascal_triangle(n):
    ''' function '''
    if n <= 0:
        return []
    else:
        lst = []
        for i in range(1, n+1):
            C = 1
            l = []
            for j in range(1, i+1):
                l.append(C)
                C = C * (i - j) // j
            lst.append(l)
        return lst
