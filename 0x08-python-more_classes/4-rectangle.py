#!/usr/bin/python3
"""
mudle doc
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        init
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        str
        """
        if (self.__height == 0 or self.__width == 0):
            return ''
        return ((self.__width * '#' + '\n') * (self.__height - 1) +
                self.__width * '#')

    def __repr__(self):
        """
        reipr
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """
        returns the value of private atr width
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        set the value of private atr width
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """
        returns the value of private atr height
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        set the value of private atr height
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)
