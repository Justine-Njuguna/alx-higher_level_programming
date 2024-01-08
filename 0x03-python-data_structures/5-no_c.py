#!/usr/bin/python3

def no_c(my_string):
    string_filter = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            string_filter += char
    return string_filter
