#!/usr/bin/python3
def simple_delete(dic, k):
    if k in dic:
        dic.pop(k)
        return dic
    else:
        return dic
