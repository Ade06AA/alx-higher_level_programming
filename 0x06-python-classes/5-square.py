#!/usr/bin/python3
""" a modle """


class Square():

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        print the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        return the value of selfe
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set self
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print the square
        """
        pass
