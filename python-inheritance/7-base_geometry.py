#!/usr/bin/python3

"""
empty class BaseGeometry
"""


class BaseGeometry():
    """
    class with integer validator
    """

    def area(self):
        """
        Raise exception of a method thats not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
