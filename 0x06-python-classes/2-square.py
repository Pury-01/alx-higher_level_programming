#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represents a Square.

    Attributes:
    _size (int): The size of the Square.
    """
    def __init__(self, size=0):
        """Initialization of new Square.

        Agrs:
        size (int): The size of the new Square created.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
