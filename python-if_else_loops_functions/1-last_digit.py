#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = number % 10
if number < 0:
    no = no - 10
if no == 0:
    print("Last digit of", number, "is", no, "and is 0")
elif no > 5:
    print("Last digit of", number, "is", no, "and is greater than 5")
else:
    print("Last digit of", number, "is", no, "and is less than 6 and not 0")
