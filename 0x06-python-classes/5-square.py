#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represents a square.

    Attributes:
    _size (int): The size of the square.
    """
    def __init__(self, size):
        """Initialize a new sqaure.


        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current are of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
