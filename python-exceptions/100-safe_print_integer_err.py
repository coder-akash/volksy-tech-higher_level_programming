#!/usr/bin/python3
import sys
def safe_print_integer_err(val):
    try:
        print('{:d}'.format(val))
        return True
    except ValueError as err:
        print('Exception :', err, file=sys.stderr)
        return False
    except TypeError as err:
        print('Exception :', err, file=sys.stderr)
        return False
