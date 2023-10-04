#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in new_list:
        if new_list[i] % 2 == 0:
            new_list[i] = True
            i += 1
        elif new_list[i] % 2 != 0:
            new_list[i] = False
            i += 1
    return (new_list)
