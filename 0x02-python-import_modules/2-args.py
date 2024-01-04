#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argv_len, "s" if argv_len > 1 else ""))
        for i in range(1, argv_len + 1):
            print("{}: {}".format(i, sys.argv[i]))
