#!/usr/bin/python3
def uppercase(str):
    upper_ch = ''
    for i in str:
        if ord(i) > 96:
            upper_ch = upper_ch + chr(ord(i)-32)
        else:
            upper_ch += i
    print('{}'.format(upper_ch))
