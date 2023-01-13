#!/usr/bin/python3
''' task 5 '''


class BaseGeometry():
    ''' class '''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('%s must be an integer' %name)
        if value <= 0:
            raise ValueError('%s must be greater than 0' %name)
