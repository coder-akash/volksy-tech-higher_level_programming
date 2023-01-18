#!/usr/bin/python3
''' task 7 '''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


with open('add_item.json', 'w') as fp:
    lst = list(load_from_json_file(fp))
    i = sys.argv[1:]
    lst += i
    save_to_json_file(lst, fp)
