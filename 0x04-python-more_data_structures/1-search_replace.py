#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return []

    result = [replace if item == search else item for item in my_list]

    return result
