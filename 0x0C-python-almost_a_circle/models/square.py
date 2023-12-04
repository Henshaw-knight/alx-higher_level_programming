#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances of Square class with given attributes
        Args:
            size (int): the size of the square
            x (int, optional): the horizontal position of the square object
            y (int, optional): the vertical position of the square object
            id (int): id of the square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the string representation of the square object"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """Size getter
        Returns:
            the size of the square object
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        Args:
            value (int): the value to set size to.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
