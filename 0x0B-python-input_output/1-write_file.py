#!/usr/bin/python3
"""Module to write a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string a text-file(utf-8) and returns the number of chars"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
