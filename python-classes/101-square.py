#!/usr/bin/python3
""" defining class """


class Square:
    """ define private attribute return area (using proprty,setter) and
    return with # (size of area)also with spaces using position(tuple) """

    def __init__(self, s=0, p=(0, 0)):
        """ constructor """
        self.size = s
        self.position = p

    @property
    def size(self):
        """ return """
        return self.__size

    @property
    def position(self):
        """ return """
        return self.__position

    @size.setter
    def size(self, size):
        """ size validation """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        pass
        """ logic of tuple """
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        """ area """
        return self.__size**2

    def __str__(self):
        """ printing # """
        if self.__size == 0:
            return (" ")
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                    if self.__position[0] > 0:
                        if i == self.__size - 1:
                            return(' '*self.__position[0]+'#'*self.__size)
                        print(' '*self.__position[0]+'#'*self.__size)
                    else:
                        if i == self.__size - 1:
                            return ('#' * self.__size)
                        else:
                            print('#' * self.__size)
