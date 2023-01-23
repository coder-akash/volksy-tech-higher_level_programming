#!/usr/bin/python3
""" task 0 """
import json as j


class Base:
    ''' class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, lst_obj):
        new = [i.to_dictionary() for i in lst_obj]
        with open(cls.__name__+'.json', 'w'):
            f.write(Base.to_json_string(new))

    @staticmethod
    def to_json_string(l_d):
        if l_d is None or len(l_d) == 0:
            return j.dumps([])
        else:
            return j.dumps(l_d)
