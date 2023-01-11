#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute return area (using proprty,setter) and
    print with # size of area'''
    def __init__(self, s=0):
        self.size = s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        def size(self, val):
            if type(val) != int:
                raise TypeError('size must be an integer')
            elif val < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = val

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else: 
            for i in range(self.__size):
                print('#' * self.__size)
