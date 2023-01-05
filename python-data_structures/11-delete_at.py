#!/usr/bin/python3
def delete_at(my_list, idx):
    val = my_list[idx]
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        my_list.remove(val)
        return my_list
