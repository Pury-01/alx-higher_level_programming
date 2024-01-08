#!/usr/bin/python3
def print_list_integer(my_list=[]):
    last_index = my_list[-1]

    for i in range(0, last_index, 1):
        print("{}".format(my_list[i]))
