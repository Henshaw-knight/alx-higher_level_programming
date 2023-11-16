#!/usr/bin/python3
"""say_my_name function Module"""


def say_my_name(first_name, last_name=""):
    """Function that prints the first name and last name in the
    required manner

    Args:
        first_name (str): the first name
        last_name (str): the last name
    Raises:
        TypeError: if `first_name` or `last_name` is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
