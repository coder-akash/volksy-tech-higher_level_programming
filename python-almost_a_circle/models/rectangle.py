#!/usr/bin/python3
""" task 2 """
import Base


class Rectangle(Base):
    ''' class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y
