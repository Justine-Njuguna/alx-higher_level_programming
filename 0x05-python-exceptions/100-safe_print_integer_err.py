#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as e:
        if "'d'" in str(e):
            print("Exception: {}".format(e), file=sys.stderr)
        else:
            print("{} is not an integer".format(value), file=sys.stderr)
        return False

