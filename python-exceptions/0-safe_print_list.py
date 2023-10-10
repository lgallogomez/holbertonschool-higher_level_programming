#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listl = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            listl += 1
        print("")
    except:
        pass
        print("")
    return (listl)
