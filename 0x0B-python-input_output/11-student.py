#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names
            to be retrieved (default: None).

        Returns:
            dict: A dictionary containing the specified
            attribute names and their values. If attrs is None,
            returns a dictionary containing all attributes and their values.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance based on the provided dictionary.

        Args:
            json (dict): A dictionary representing
            the attributes and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
