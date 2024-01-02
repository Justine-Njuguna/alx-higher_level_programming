#!/usr/bin/python3

def uppercase(input_str):
    """
    Convert a string to uppercase.

    Args:
    - input_str: the input string

    Returns:
    - The input string converted to uppercase
    """
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char

    print(result, end='\n')


if __name__ == "__main__":
    uppercase("Hello, World!")
