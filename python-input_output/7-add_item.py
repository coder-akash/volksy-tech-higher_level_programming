#!/usr/bin/python3
''' task 7 '''
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    with open('add_item.json','r+') as fp:
        if len(fp.read()) == 0:
            save_to_json_file([], "add_item.json")
        else:
            vals = load_from_json_file("add_item.json")
            for i in sys.argv[1:]:
                vals.append(i)
            save_to_json_file(vals, "add_item.json")
