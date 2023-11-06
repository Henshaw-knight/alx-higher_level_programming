#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an instance
    of the specified class; otherwise False
    Args:
        obj (object): instance of a class
        a_class (class): class from which the object can be formed/instantiated
    """
    if type(obj) is a_class:
        return True
    else:
        return False
