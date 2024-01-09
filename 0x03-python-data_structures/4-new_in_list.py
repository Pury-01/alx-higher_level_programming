#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    my_list1 = list(my_list)

    if idx < 0 or idx >= len(my_list):
        return my_list1

    else:
        my_list1[idx] = element
        return my_list1
