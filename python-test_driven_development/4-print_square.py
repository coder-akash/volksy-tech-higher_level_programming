#!/usr/bin/python3
''' Write a function that prints a square with the character #. '''


def print_square(size):
    ''' print_square '''

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#'*size)
