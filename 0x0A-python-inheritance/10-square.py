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
