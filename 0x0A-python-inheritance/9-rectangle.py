#!/usr/bin/python3
"""
Module docs
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class docs
    """

    def __init__(self, width, height):
        """
        initialization
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        func doc
        """
        return self.__width * self.__height

    def __str__(self):
        """
        func doc
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
