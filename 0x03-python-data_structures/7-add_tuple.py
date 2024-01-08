#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # use 0 for each missing int
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the sum of corresponding elements
    return (a[0] + b[0], a[1] + b[1])
