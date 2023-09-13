#!/usr/bin/python3
"""
module doc
"""


class Student:
    """
    class doc
    """

    def __init__(self, fn, ln, age):
        """
        func doc
        """
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self):
        """
        func doc
        """
        return self.__dict__
