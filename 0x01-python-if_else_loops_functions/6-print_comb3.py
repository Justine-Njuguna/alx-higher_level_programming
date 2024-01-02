#!/usr/bin/python3

for x in range(10):
    for y in range(x + 1, 10):
        if x < 8:
            print("{:d}{:d}, ".format(x, y), end="")
        else:
            print("{:d}{:d}".format(x, y))
