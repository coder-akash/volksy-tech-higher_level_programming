#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute return area (using proprty,setter) and
    print with # (size of area)also with spaces using position(tuple)'''

    def __init__(self, s=0, p=(0, 0)):
        self.__size = s
        self.__position = p

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, val):
            if type(val) != int:
                raise TypeError('size must be an integer')
            elif val < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = val

    @position.setter
    def position(self, val):
        if type(val) != tuple and type(t[0]) != int and type(t[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = val

    def area(self):
        return self.size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] >= 0:
                    print(''*self.__position[0], end="")
                print('#' * self.__size)