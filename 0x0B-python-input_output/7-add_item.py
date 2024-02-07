#!/usr/bin/python3
"""Script to add cli args to a Python list and save them to a file."""


import sys


def main():
    # Import save_to_json_file and load_from_json_file dynamically
    
    save_module = __import__('save_to_json_file')
    load_module = __import__('load_from_json_file')

    # Check if add_item.json already exists, if not create an empty list

    try:
        items = load_from_json_file("add_item.json")

    except FileNotFoundError:
        items = []

    # Add command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the list to a file in JSON format
    save_to_json_file(items, "add_item.json")
