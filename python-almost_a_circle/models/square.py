#!/usr/bin/python3
""" square task """
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self,val):
        self.width = val
        self.height = val

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format
                (self.id, self.x, self.y, self.width))
