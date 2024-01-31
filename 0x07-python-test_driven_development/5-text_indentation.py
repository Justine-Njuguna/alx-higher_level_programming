#!/usr/bin/python3


def text_indentation(text):
    """Prints a text with 2 new lines after each of these chars: ., ? and :"""

    if not isinstance(text, str):
        """Raises a TypeError where text is a string"""

        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in [punctuations]:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
