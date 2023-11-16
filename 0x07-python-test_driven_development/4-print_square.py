#!/usr/bin/python3
"""print_square function module"""


def print_square(size):
    """Prints a square with the character #
    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if the size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()

        if size == 0:
            print()
