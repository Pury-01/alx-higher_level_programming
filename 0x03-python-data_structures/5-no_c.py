#!/usr/bin/python3


def no_c(my_string):
    character_removed = "cC"

    new_string = ''
    for char in my_string:
        if char not in character_removed:
            new_string += char

    return new_string
