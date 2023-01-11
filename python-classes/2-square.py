#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute with exception handling'''
    def __init__(self, s=0):
        try:
            if type(s) != int:
                raise TypeError('size must be an integer')
            elif s < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = s
        finally:
            pass
