#!/usr/bin/python3
def sq(lst):
    return list(map(lambda a: a ** 2, lst))
def square_matrix_map(mat):
    return list(map(sq, mat))
