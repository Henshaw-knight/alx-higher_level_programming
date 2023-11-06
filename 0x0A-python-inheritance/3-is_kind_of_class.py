#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class, otherwise False
    Args:
        obj (objeect): instance of a class or its subclass
        a_class (class): class from which the object can be instantiated
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
