#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute with exception handling'''
    def __init__(self, s=0):
        try:
            if type(s) != int:
                raise TypeError
            elif s < 0:
                raise ValueError
            else:
                self.__size = s
        except TypeError:
            print('size must be an integer')
        except ValueError:
            print('size must be >= 0')
