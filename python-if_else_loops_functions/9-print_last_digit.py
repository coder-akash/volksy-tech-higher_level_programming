#!/usr/bin/python3
final = ''
def print_last_digit(number):
    global final
    lst_no = abs(number) % 10
    final += str(lst_no)
    return final
