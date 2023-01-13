#!/usr/bin/python3
''' task 5 '''


class Rectangle(BaseGeometry):
    ''' class '''

    def __init__(self, width, height):
        self.__width = BaseGeometry().integer_validator('width', width)
        self.__height = BaseGeometry().integer_validator('height', height)
