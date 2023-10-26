#!/usr/bin/python3

"""
class square inherits from Rectangle
"""


class Square(__import__('9-rectangle').Rectangle):
    """
    class inherits from Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size

    def area(self):
        return(self.size ** 2)

    def __str__(self):
        return(f"[{__class__.__name__}] {self.size}/{self.size}")