#!/usr/bin/python3
def square_matrix_simple(mat):
    new_mat = []
    for i in mat:
        lst = list(map(lambda n: n**2, i))
        new_mat.append(lst)
    return new_mat
