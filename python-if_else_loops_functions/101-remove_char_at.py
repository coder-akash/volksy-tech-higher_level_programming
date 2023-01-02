#!/usr/bin/python3
def remove_char_at(str, n):
    lst = list(i for i in str)
    lst.pop(n)
    st=''
    for j in lst:
        st += j
    return st
