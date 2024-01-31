#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """prints my name {first name and {last name}"""

    if not isinstance(first_name, str):
        """Raises a TypeError if the first name is not a string"""

        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        """Raises a TypeError if the last name is not a string"""

        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))

    else:
        print("My name is {}".format(first_name))
