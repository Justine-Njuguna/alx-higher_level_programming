#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers, a and b of either float or int"""

    if not (isinstance(a, int) or isinstance(a, float)):
        """Raises a typeerror if the num is not an int or float"""

        raise TypeError("a must be an integer or a float")

    if not (isinstance(b, int) or isinstance(b, float)):
        """Raises a typeerror if the num b is not an int or float"""

        raise TypeError("b must be an integer or a float")

    return int(a) + int(b)
