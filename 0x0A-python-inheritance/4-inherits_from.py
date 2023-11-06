#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False

    Args:
        obj (object): the objec to checkt
        a_class (class): the specified class
    """
    if issubclass(type(obj), a_class) and (type(obj) is not a_class):
        return True
    return False
