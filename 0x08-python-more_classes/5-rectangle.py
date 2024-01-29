#!/usr/bin/python3


"""Define a class Rectangle."""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """"Retrieves the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Find the area of the rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Finds the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return (0)
        return ((self._width * 2) + (self.height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ("")
        rect = ['#' * self._width for _ in range(self._height)]
        return ("\n".join(rect))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self._width)
        rect += ", " + str(self._height) + ")"
        return (rect)

    def __del__(self):
        """Prints a deletion message whenever deletion of Rectangle occurs."""
        print("Bye rectangle...")
