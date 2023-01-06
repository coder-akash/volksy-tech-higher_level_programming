#!/usr/bin/python3
def complex_delete(d, ele):
    if ele in d.values():
        for i in list(d.keys()):
            if d[i] == ele:
                d.pop(i)
        return d
    else:
        return d
