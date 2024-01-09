#!/usr/bin/python3
def print_list_integer(my_list=[]):
    #last_index = my_list[-1]

    for i in range(0, len(my_list), 1):
        print("{:d}".format(my_list[i]))
