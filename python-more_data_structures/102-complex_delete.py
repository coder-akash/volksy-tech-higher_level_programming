#!/usr/bin/python3
def complex_delete(d, ele):
    new_dic = {}
    if ele in d.values():
        for i, j in d.items():
            if j != ele:
                new_dic[i] = j
        return new_dic
    else:
        return d
