#!/usr/bin/python3
"""dictionary desc with simple data structure for JSON serialization"""


def class_to_json(obj):
    """Returns above description"""

    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
        elif isinstance(value, (tuple, set)):
            # Convert tuples and sets to lists
            json_dict[key] = list(value)
    return json_dict
