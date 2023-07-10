#!/usr/bin/python3
"""
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """
    Represents a base geometry.
    """

    def area(self):
        """
        Computes the area.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
