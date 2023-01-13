#!/usr/bin/python3
''' Task :function that returns True if the object is exactly an instance of
the specified class ; otherwise False.'''


def is_same_class(obj, a_class):
    ''' Function '''
    
    if type(obj) == a_class:
        return True
    else:
        return False
