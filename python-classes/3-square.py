#!/usr/bin/python3

""" File where I'm creating a class """


class Square:
    """ class square creates a private attribute """
    def __init__(self, __size=0):
        self.__size = __size
        if type(__size) != int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        a = self.__size * self.__size
        return (a)
