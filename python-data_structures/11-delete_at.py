#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_l = list()
    i = 0
    for i in range(len(my_list)):
        if i != idx:
            new_l.append(my_list[i])
            i += 1
        else:
            i += 1
    return (new_l)
