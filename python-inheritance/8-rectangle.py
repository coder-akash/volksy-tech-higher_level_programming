#!/usr/bin/python3
''' task 5 '''


class Rectangle(BaseGeometry):
    ''' class '''

    def __init__(self, width, height):
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)
