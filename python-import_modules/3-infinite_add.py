#!/usr/bin/python3
import sys
from sys import argv


def func():
    i = 0
    summ = 0
    args = sys.argv

    if len(sys.argv) == 1:
        print("{}".format(0))
    elif len(sys.argv) == 2:
        print("{}".format(args[1]))
    elif len(sys.argv) > 2:
        for i in range(1, len(args)):
            summ = summ + int(args[i])
        print(summ)


if (__name__ == "__main__"):
    func()
