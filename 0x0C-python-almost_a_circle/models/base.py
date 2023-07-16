#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""

import unittest


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
