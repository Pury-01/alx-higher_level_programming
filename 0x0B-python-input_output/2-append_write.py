#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): the string to append.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
