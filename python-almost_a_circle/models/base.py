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

    @staticmethod
    def to_json_string(l_d):
        if l_d is None or len(l_d):
            return j.dumps([])
        else:
            return j.dumps(l_d)
