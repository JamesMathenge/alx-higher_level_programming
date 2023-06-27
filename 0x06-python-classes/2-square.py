#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    A class that defines a square.

    Attributes:
         __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (default: 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
