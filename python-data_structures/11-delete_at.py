#!/usr/bin/python3
def delete_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list = my_list[:idx] + my_list[idx+1:]
        return my_list
