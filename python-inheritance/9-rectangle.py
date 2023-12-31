#!/usr/bin/python3

"""
class inherits BaseGeometry class
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):

    """
    class inherits BaseGeometry class, returns area and prints
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return(f"[{__class__.__name__}] {self.__width}/{self.__height}")
