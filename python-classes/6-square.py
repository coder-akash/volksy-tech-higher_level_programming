#!/usr/bin/python3
''' defining class '''


class Square:
    ''' define private attribute return area (using proprty,setter) and
    print with # (size of area)also with spaces using position(tuple)'''

    def __init__(self, s=0, p=(0, 0)):
        self.size = s
        self.position = p

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2 or type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0 and self.__position[1] > 0:
                    print(' '* self.__position[0] +'#' * self.__size + ' '*self.__position[1])
                elif self.__position[0] > 0:
                    print(' ' * self.__position[0] + '#' * self.__size)
                elif self.__position[1] > 0:
                    print('#' * self.__size + ' '*self.__position[1])
                else:
                    print('#' * self.__size)
