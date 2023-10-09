#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    new_list = []
    new_list = list_1 + list_2
    new_set = set(new_list)
    return (new_set)
