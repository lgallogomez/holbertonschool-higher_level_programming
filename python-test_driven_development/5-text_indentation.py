#!/usr/bin/python3
"""
Function prints a text with 2 new lines
"""


def text_indentation(text):
    """
    function prints a text with 2 new lines
    """

    new_str = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    chars = ".?:"
    while (i < len(text)):
        if text[i] in chars:
            print(text[i], end="\n\n")
            if i < (len(text) - 1) and text[i + 1] == " ":
                i += 2
            else:
                i += 1
        else:
            print(text[i], end="")
            i += 1
