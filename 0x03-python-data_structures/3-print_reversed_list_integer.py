#!/usr/bin/bash

def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num))
