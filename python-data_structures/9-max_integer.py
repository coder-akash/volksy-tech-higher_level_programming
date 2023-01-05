#!/usr/bin/python3
def max_integer(lst):
    if len(lst) == 0:
        return None
    else:
        max = 0
        for i in lst:
            if max < i:
                max = i
        return max
