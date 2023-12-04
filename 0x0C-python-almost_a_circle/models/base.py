#!/usr/bin/python3
"""Base class module"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns JSON representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)
