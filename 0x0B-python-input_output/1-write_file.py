#!/usr/bin/python3
"""DEfine a function for file-writing."""


def write_file(filename="", text=""):
    """writes a string to a text file.

    Args:
        filename (str): The name of the file to write.
        Text (str): The text to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
