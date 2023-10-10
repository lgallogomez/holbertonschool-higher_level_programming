#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listLen = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            listLen += 1
        print("")
    except:
        pass
    print("")
    return (listLen)

my_list = [1, 2, 3, 4]
x = len(my_list) + 1

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))