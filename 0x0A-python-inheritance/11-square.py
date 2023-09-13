#!/usr/bin/python3
"""
Module docs
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class docs
    """
    def __init__(self, size):
        """
        initialization
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        func doc
        """
        return super().area()

    def __str__(self):
        """
        func doc
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
