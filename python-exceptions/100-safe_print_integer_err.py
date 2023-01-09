#!/usr/bin/python3
def safe_print_integer_err(val):
    try:
        print('{:d}'.format(val))
        return True
    except ValueError as err:
        print('Exception: ', err)
        return False
    except TypeError as err:
        print('Exception: ', err)
        return False
