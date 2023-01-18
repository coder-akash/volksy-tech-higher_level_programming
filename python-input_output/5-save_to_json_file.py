#!/usr/bin/python3
''' task 5 '''
import json as js


def save_to_json_file(my_obj, filename):
    ''' function '''
    with open(filename, 'w') as fp:
        js.dump(my_obj, fp)
