#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # Exclude the script name
    plural = "arguments" if num_args > 1 else "argument"

    print(f"{num_args} {plural}{':' if num_args > 0 else '.'}")

    if num_args > 0:
        for i, arg in enumerate(sys.argv[1:]):  # Start from index 1
            print(f"{i + 1}: {arg}")

