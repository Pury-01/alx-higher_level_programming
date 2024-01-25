#!/usr/bin/python3


"""Define a class Square."""


class Square:
    """Represents a square.

    Attributes:
    __size (int): The size of the square.
    __position (int, int): position of the square.

    Methods:
    area(): Calculates the area of the square.
    my_print(): Prints square using '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new sqaure.


        Args:
            size (int): The size of the new square.
            position (int, int): position of new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current are of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__position[0])]
            [print("#", end="") for x in range(0, self.size)]
            print("")
