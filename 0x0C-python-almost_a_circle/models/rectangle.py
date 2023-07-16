#!/usr/bin/python3
"""Defines a Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        """

        super().__init__(id)  # Call the super class with id

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Define getter and setter methods for width, height, x, and y

    @property
    def width(self):
        """
        Getter for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
