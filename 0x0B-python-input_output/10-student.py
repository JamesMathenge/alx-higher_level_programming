#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """
    A class representing a Student.

    Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
    """

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
            attrs (list):list of attribute names retrieved (default: None).

        Returns:
            dict: dictionary containing specified attribute names
            and their values if attrs is None,
            returns a dictionary containing all attributes and their values.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
