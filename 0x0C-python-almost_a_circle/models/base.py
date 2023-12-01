#!/usr/bin/python3
"""Base class module"""


class Base:
    """The base class for other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class instances with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
