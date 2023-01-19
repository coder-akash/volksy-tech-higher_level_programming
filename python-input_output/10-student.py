#!/usr/bin/python3
''' task 10 '''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,attrs=None):
        ''' function '''
        if attrs == None:
            return self.__dict__
        else:
            temp = {}
            for i in attrs:
                if i in self.__dict__:
                    temp[i] = self.__dict__.get(i)
            return temp
