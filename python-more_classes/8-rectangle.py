#!/usr/bin/python3
''' task 8 '''


class Rectangle:
    '''class '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError('width must be an integer')
        elif val < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = val

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError('height must be an integer')
        elif val < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = val

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            res = rect_1
        elif rect_1.area() > rect_2.area():
            res = rect_1
        else:
            res = rect_2
        return res

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        else:
            for i in range(self.__height):
                if i == self.__height - 1:
                    return (str(self.print_symbol) * self.__width)
                else:
                    print(str(self.print_symbol) * self.__width)

    def __repr__(self):
        return ("Rectangle("+str(self.__width)+", "+str(self.__height)+")")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
