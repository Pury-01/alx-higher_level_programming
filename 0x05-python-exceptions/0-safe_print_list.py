#!/usr/bash/python3


def safe_print_list(my_list=[], x=0):
    elements_to_print = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            elements_to_print += 1
    except IndexError:
        pass

    print()

    return(elements_to_print)
