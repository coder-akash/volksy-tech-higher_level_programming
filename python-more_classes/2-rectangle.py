#!/usr/bin/python3
''' task 2 '''


class Rectangle:
    '''class '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError('width must be an integer')
        elif val < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = val

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError('height must be an integer')
        elif val < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = val

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)
