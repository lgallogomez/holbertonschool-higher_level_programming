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
    for element in range(len(text)):
            if text[element] != '.' and text[element] != '?' and text[element] != ':':
                new_str += text[element]
            else:
                new_str += text[element]
                element += 1
                new_str += '\n'
                new_str += '\n'
    print (new_str)
