#!/usr/bin/python3
''' task 4 '''


def inherits_from(obj, a_class):
    ''' Function '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
