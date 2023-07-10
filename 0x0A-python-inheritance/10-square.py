#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
        str: The string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
