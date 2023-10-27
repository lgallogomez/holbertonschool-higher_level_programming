#!/usr/bin/python3

"""
function prints full name
"""


def say_my_name(first_name, last_name=""):
    """
    function prints full name
    """
    if type(first_name) is not str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name == "":
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
