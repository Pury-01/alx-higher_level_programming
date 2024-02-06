#!/usr/bin/python3
"""Define a function for file-reading."""


def read_file(filename=""):
    """print the contents of the text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
