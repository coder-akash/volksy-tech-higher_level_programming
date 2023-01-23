#!/usr/bin/python3
""" task rectangle """
from models.base import Base


class Rectangle(Base):
    ''' class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = val

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = val

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = val

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError('y must be an integer')
        elif val < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = val

    def area(self):
        ''' area of rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' display '''
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x + '#' * self.__width)
            else:
                print('#' * self.__width)

    def update(self, **kwargs):
        ''' update '''
        for i, j in kwargs.items():
            setattr(self, i, j)

    def to_dictionary(self):
        ''' return dict format '''
        d = self.__dict__
        new_d = {}
        for i, j in d.items():
            if len(i) > 2:
                new_d[i[12:]] = j
            else:
                new_d[i] = j
        return new_d

    def __str__(self):
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format
                (self.id, self.__x, self.__y, self.__width, self.__height))
