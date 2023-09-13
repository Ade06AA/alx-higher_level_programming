#!/usr/bin/python3
"""
Module docs
"""


class BaseGeometry():
    """
    My docs
    """

    def area(self):
        """
        func doc
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        func doc
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
