#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute if its not satisfy the conditions raise some
    errors and return area (using proprty,setter) also comparing size of
    two class obj'''

    def __init__(self, s=0):
        self.size = s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val

    def area(self):
        ''' returning the area of size w.r.t size '''
        return (self.__size**2)

    ''' compasrison methods '''

    def __eq__(self, other):
        return (self.size) == (other.size)

    def __nq__(self, other):
        return (self.size) != (other.size)

    def __lt__(self, other):
        return (self.size) < (other.size)

    def __gt__(self, other):
        return (self.size) > (other.size)

    def __le__(self, other):
        return (self.size) <= (other.size)

    def __ge__(self, other):
        return (self.size) >= (other.size)
