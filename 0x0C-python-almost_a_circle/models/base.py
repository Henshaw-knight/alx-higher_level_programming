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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Filename is <Class name>.json
        Args:
            list_objs (list): list of instances that inherits Base
        """
        filename = f"{cls.__name__}.json"
        obj_dict_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_dict_list.append(obj.to_dictionary())
        json_data = cls.to_json_string(obj_dict_list)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string`"""
        if json_string is None or len(json_string) == 0:
            return([])
        return json.loads(json_string)
