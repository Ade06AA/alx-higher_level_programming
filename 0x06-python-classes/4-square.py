#!/usr/bin/python3
"""
class modle
"""


class Square():
    """
    square class
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        return area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
