#!/usr/bin/python3
def remove_char_at(str, n):
    lst = list(i for i in str)
    #print(len(lst))
    if n >= 0 and len(lst) >= n:
        lst.pop(n)
    st = ''
    for j in lst:
        st += j
    return st
