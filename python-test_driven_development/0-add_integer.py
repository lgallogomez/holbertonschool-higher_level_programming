#!/usr/bin/python3

'''
Function adds 2 integers. b setted as 98 if nothing is provided
'''


def add_integer(a, b=98):

    """
    Function adds 2 integers. b setted as 98 if nothing is provided
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return c
