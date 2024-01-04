#!/usr/bin/python3
from magic_calculation_102 import add, sub  # Import necessary functions

def magic_calculation(a, b):
    """Performs a calculation based on the values of a and b."""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):  # Iterate from 4 to 5 (inclusive)
            c = add(c, i)
        return c
    else:
        return sub(a, b)
