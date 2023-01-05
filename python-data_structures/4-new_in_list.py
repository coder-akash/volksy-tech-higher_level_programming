#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    copy = my_list.copy()
    if idx < 0:
        return copy
    elif idx > len(my_list) -1:
        return my_list
    else:
        my_list[idx] = new_element
        return my_list
