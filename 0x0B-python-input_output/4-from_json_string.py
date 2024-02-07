#!/usr/bin/python3
"""Module to return an object represented by a JSON string."""


import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string."""

    return json.loads(my_str)
