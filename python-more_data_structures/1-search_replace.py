#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search: 
            my_list[i] = replace
    return (new_list)
