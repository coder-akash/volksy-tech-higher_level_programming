#!/usr/bin/python3
''' task 7 '''
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = (__import__('6-load_from_json_file').
            load_from_json_file)
    with open('add_item.json','w') as fp:
        save_to_json_file([], "add_item.json")
        vals = load_from_json_file("add_item.json")
        vals.extend(sys.argv[1:])
        save_to_json_file(vals, "add_item.json")
