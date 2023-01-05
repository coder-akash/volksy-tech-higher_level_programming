#!/usr/bin/python3
def delete_at(lst, idx):
    if idx < 0 or idx > len(lst):
        return lst
    else:
        return lst[:idx+1] + lst[idx+1:]
