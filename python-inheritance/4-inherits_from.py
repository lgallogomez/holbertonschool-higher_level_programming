#!/usr/bin/python3

"""
returns True if object is instance of class inherited (directly or indirectly) specified class
"""


def inherits_from(obj, a_class):
    """
    returns True if object is instance of class inherited (directly or indirectly) class
    """

    if type(obj) is a_class:
        return False

    if issubclass(type(obj), a_class):
        return True

    return False
