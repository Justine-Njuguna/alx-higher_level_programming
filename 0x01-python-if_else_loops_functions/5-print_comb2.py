#!/usr/bin/python3

for nums in range(100):
    if nums < 99:
        print("{:02d}, ".format(nums), end="")
    else:
        print("{:02d}".format(nums))
