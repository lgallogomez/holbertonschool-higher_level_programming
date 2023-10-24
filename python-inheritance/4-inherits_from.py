#!/usr/bin/python3

"""
returns True if the object is an instance of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class
    """
    
    if type(obj) is a_class:
        return False
    
    if issubclass(type(obj), a_class):
        return True
    
    return False
