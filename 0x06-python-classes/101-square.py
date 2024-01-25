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
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): position of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
        value (int): Size value to set.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

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
        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print("#", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(0, self.size)]
            print("")

    def __str__(self):
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()
