#!/usr/bin/python3
''' task 12 '''


def pascal_triangle(n):
    ''' function '''
    if n <= 0:
        return []
    else:
        for i in range(n+1):
            l = [int(j) for j in str(11 ** i)]
            if i == n:
                return l
            else:
                print(l)
