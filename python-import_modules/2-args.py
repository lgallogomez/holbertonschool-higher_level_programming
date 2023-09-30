#!/usr/bin/python3
import sys
from sys import argv


def func():
    i = 0
    args = sys.argv
    if len(sys.argv) == 1:
            print("{} arguments.".format(i))
    elif len(sys.argv) == 2:
        print("{} argument:".format(i + 1))
        print("{}: {}".format((i + 1), args[i + 1]))
    elif len(sys.argv) > 2:
        print("{} arguments:".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))


if (__name__ == "__main__"):
    func()
