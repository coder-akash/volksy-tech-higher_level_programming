#!/usr/bin/python3
""" task 2 """
from models.base import Base


class Rectangle(Base):
    ''' class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(id)
