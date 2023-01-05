#!/usr/bin/python3
def print_matrix_integer(mat):
    print(mat,len(mat))
    for i in range(len(mat)):
        for j in mat[i]:
            print('{:d}'.format(j), end=" ")
        print()
