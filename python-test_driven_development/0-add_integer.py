#!/usr/bin/python3

'''
Function adds 2 integers. b setted as 98 if nothing is provided
'''


def add_integer(a, b=98):

    """
    Function adds 2 integers. b setted as 98 if nothing is provided
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
    
