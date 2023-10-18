#!/usr/bin/python3
""" File where im creating a class called Rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be and integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
