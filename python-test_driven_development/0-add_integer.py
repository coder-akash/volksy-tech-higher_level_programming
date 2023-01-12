''' The program return desire output '''

def add_integer(a, b=98):
    ''' This function returns the addition of a, b '''
    if isinstance(a, (int, float)) is not True:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is not True:
        raise TypeError('b must be an integer')
    return a+b
