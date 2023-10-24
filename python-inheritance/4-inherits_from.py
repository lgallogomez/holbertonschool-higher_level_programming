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
    
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
