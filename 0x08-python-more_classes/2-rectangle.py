#!/usr/bin/python3

"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initiliaze a new Rectangle.

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
            raise TypeError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieves the height of new rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value,  int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return (0)
        return ((self._width * 2) + (self._height * 2))
