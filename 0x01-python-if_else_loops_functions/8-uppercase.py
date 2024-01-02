#!/usr/bin/python3

def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
    - s: input string

    Returns:
    - None
    """
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase using ASCII values
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()  # Print a new line


if __name__ == "__main__":
    uppercase("best")  # Output: BEST
    uppercase("Best School 98 Battery street")
