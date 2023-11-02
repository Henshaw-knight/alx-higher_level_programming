#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Class with no class or object attribute, that prevents the user
    from dynamically creating new instance attributes, except if the new
    instance attribute is called first_name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Initializes object"""
        pass
