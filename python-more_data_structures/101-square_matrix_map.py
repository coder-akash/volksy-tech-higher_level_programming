#!/usr/bin/python3
def square_matrix_map(mat):
    return list(map(lambda l: list(map(lambda x: x ** 2, l)), mat))
