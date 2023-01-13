#!/usr/bin/python3
''' task 9 '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class '''

    def __init__(self, width, height):
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
