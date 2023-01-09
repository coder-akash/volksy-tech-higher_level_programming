#!/usr/bin/python3
def safe_print_integer_err(val):
    try:
        print('{:d}'.format(val))
        return True
    except Exception as err:
        return False
        print('Exception: ', err)
