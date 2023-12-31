#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    j = 0
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[j]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            j += 1
    return (new_list)
