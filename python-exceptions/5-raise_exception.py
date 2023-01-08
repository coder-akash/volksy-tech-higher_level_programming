class raise_exception(Exception):
    pass
try:
    raise raise_exception
except raise_exception:
    print("Exception raised")
