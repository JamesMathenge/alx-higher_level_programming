#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""

import unittest
import json


class Base:
    """Represent the base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize object with an id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)
