#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = new_element
        return my_list
