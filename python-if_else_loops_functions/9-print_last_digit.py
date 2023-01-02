#!/usr/bin/python3
def print_last_digit(number):
    lst_no = number % 10
    if number < 0:
        lst_no = lst_no - 10
    return lst_no
