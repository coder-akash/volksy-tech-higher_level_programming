#!/usr/bin/python3
""" task 2 """
from models.base import Base


class Rectangle(Base):
    ''' class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
