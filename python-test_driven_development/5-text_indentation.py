#!/usr/bin/python3
"""Module for text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after specified characters.

    The target characters are: ., ? and :

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Flag to skip spaces at the beginning of a line
    skip_space = True

    for char in text:
        if skip_space and char == " ":
            continue

        print(char, end="")
        skip_space = False

        if char in [".", "?", ":"]:
            print("\n")
            skip_space = True
