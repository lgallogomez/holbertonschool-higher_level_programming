#!/usr/bin/python3

"""
empty class BaseGeometry
"""


class BaseGeometry():
    """
    no methods so far
    """

    def area(self):
        raise Exception("area() is not implemented")

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))