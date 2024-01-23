#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_to_print = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            element_to_print += 1

        except IndexError:
            break
    print("")
    return (element_to_print)
