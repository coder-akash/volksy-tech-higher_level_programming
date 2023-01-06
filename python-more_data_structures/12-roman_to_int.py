#!/usr/bin/python3
def roman_to_int(st):    
    d1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    if type(st) == str:
        for i in range(len(st)):
                val = d1[st[i]]
                if i+1 < len(st) and d1[st[i+1]] > val:
                    sum = sum - val
                else:
                    sum = sum + val
        return sum
    else:
        return 0
