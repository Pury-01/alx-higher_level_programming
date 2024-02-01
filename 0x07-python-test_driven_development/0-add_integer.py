#!/usr/bin/python3


"""Function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers a and b.

    Args:
        a (int): first integer. cast into int if a float.
        b (int): second integer. cast into int if a float

    Raises:
        TypeError: If a or b is not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
