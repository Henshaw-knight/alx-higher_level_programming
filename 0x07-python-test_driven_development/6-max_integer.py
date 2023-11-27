#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(int_list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if type(int_list) is not list:
        raise TypeError
    if len(int_list) == 0:
        return None
    result = int_list[0]
    i = 1
    while i < len(int_list):
        if type(int_list[i]) is not int or type(int_list[0]) is not int:
            raise ValueError
        if int_list[i] > result:
            result = int_list[i]
        i += 1
    return result
