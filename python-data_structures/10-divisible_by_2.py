#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    i = 0
    while i < len(new_list):
        print("{}".format(new_list[i]))
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else: 
            new_list[i] = False
        i += 1
    return (new_list)

list = [1, 2, 3, 4]
list_result = divisible_by_2(list)

i = 0
while i < len(list):
    print("{:d} {:s} divisible by 2".format(list[i], "is" if list_result[i] else "is not"))
    i += 1
