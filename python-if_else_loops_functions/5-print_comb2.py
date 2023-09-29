#!/usr/bin/python3
for i in range(00, 100):
    form_n = "{:02d}".format(i)
    if i != 99:
        print("{}, ".format(form_n), end='')
    else:
        print("{}".format(form_n))
