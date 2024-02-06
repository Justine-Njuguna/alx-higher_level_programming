#!/usr/bin/python3
"""Module to read a text file and print its content"""


def read_file(filename=""):
    """Reads a text file(utf-8) and prints to STDOUT"""

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
