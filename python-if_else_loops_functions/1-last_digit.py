#!/usr/bin/python3
import random
no = random.randint(-10000, 10000)
lst_no = no % 10
if no < 0:
    lst_no = lst_no - 10
if lst_no > 5:
    print("Last digit of", no, "is", lst_no, "and is greater than 5")
elif lst_no == 0:
    print("Last digit of", no, "is", lst_no, "and is 0")
else:
    print("Last digit of", no, "is", lst_no, "and is less than 6 and not 0")
