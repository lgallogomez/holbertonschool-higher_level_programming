#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char = chr(ord(str[i]) - 32)
        else:
            char = str[i]
        print("{}".format(char), end="")
        i += 1
    print("")
