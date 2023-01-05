#!/usr/bin/python3
def print_matrix_integer(mat):
    for i in range(len(mat)):
        if len(mat[i]) == 0:
            print()
        for j in mat[i]:
            if j == mat[i][-1]:
                print(j)
            else:
                print('{:d}'.format(j), end=" ")
