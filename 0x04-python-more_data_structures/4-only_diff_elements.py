#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff_set = (
            {y for y in set_1 if y not in set_2} |
            {x for x in set_2 if x not in set_1}
            )

    return diff_set
