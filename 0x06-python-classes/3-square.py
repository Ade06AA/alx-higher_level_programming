#!/usr/bin/python3
""" a modle """


class Square:
    """
    class doc
    """

    def __init__(self, size=0):
        """
        class initialization
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        print the area
        """
        return self.__size * self.__size
