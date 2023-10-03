#!/usr/bin/python3
def no_c(my_string):
    targ_1 = 'c'
    targ_2 = 'C'
    new_str = ""
    for char in my_string:
        if char != targ_1 and char != targ_2:
            new_str += char
    return(new_str)
