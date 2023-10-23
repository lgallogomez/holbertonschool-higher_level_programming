#!/usr/bin/python3

"""
function returns true if object is same an instance of class, or false
"""


def is_same_class(obj, a_class):
    """
    function returns true if object is same an instance of class, or false
    """
    if isinstance(obj, a_class) == True:
        return True
    return False
