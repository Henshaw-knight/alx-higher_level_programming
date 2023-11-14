#!/usr/bin/python3
"""Module that demonstrates the addition of 2 integers"""


def add_integer(a, b=98):
    """Function that adds two number and returns the result"""
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return a + b
