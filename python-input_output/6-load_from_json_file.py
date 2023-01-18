#!/usr/bin/python3
''' task 6 '''
import json as js


def load_from_json_file(filename):
    ''' function '''
    with open(filename) as fp:
        return js.load(fp)
