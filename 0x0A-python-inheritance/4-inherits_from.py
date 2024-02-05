#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Checks if the obj, is an instance of a class that is inherited"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
