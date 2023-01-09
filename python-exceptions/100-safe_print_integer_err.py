#!/usr/bin/python3
#!/usr/bin/python3
import sys
def safe_print_integer_err(val):
    try:
        print('{:d}'.format(val))
        return True
    except ValueError as err:
        return False
        print('Exception :', err, file = sys.stderr)
    except TypeError as err:
        return False
        print('Exception :', err, file = sys.stderr)
