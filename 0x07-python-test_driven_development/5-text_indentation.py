#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    `.`, `?` and `:`
    Args:
        text (str): text that will be printed
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for index, character in enumerate(text):
        if character in ['.', '?', ':']:
            print(character, end="")
            print("\n")
        elif (character == " " and (text[index + 1] in ['.', '?', ':', ' '] or
                                    text[index - 1] in ['.', '?', ':', ' '])):
            continue
        else:
            print(character, end="")
