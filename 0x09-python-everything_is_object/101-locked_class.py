#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Class with no class or object attribute, that prevents the user
    from dynamically creating new instance attributes, except if the new
    instance attribute is called first_name
    """
    def __init__(self):
        """Initializes new object"""
        self.first_name = None

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name)
            )
