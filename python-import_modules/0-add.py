#!/usr/bin/python3
from add_0 import add


def add_f():
    a = 1
    b = 2
    add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    add_f()
