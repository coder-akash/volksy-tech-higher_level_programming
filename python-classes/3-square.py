#!/usr/bin/python3
"""defining class which returns area of square"""


class Square:
    """define private attribute with exception handling and returning
    area of square"""

    def __init__(self, s=0):
        try:
            if type(s) != int:
                raise TypeError('size must be an integer')
            elif s < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = s
    
    def area(self):
        ''' returning the area of size w.r.t size '''
        return self.__size**2
