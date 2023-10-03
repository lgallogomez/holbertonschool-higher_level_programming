#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list) - 1:
        return (my_list)
    elif idx < 0:
        return (my_list)
    else:
        new_l = my_list[:]
        new_l[idx] = element
        return (new_l)
