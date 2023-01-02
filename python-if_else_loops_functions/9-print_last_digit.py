#!/usr/bin/python3
def print_last_digit(number):
    lst_no = abs(number) % 10
    return lst_no
print(print_last_digit(98), end="")
print(print_last_digit(0), end="")
r = print_last_digit(-1024)
print(r, end="")
print(r)
