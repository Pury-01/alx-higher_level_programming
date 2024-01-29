#!/usr/bin/python3


"""Define a Rectangle class."""


class Rectangle:
    """"Represent a rectangle.

    Attributes:
    width (int): The width of a rectangle.
    height (int): The height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
        width (int): The width of new rectangle.
        height (int): The height of new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieve the width of the rectangle."""
            return self._width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            if not isisntance(value, int):
                raise TypeError("Width must be an integer")
            if value < 0:
                raise ValueError("Width must be >= 0")
            self._width = value

        @property
        def height(self):
            """Retrieves the heigth of the rectangle."""
            return self._height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle."""
            if not isinstance(value,  int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
