#!/usr/bin/python3
"""Class Student w attributes"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Inits a Student instance with first_name, last_name, and age."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""

        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""

        if attrs is None:
            return self.__dict__

        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """Replaces all attrs of the student instance based on a dict rep"""

        for key, value in json.items():
            setattr(self, key, value)
