#!/usr/bin/python3

""" File where I'm creating a class """


class Square:
    """ class square creates a private attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        a = self.__size ** 2
        return (a)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("\n", end='')
            for i in range(0, self.__size):
                print(" ", end='')
                for i in range(0, self.__size):
                    print("#", end='')
                print("")
