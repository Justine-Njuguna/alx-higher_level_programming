#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        # Create a new list excluding the element at the specified index
        return my_list[:idx] + my_list[idx + 1:]
    else:
        # Return the same list if idx is negative or out of range
        return my_list
