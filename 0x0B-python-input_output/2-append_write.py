#!/usr/bin/python3
"""Module to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a str to the end of a (UTF8) & return the num of char added."""

    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
    return chars_added
