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

    def to_json(self, attrs=None):
        """
        func doc
        """
        tt = self.__dict__
        if attrs is None:
            return tt
        else:
            t = {}
            for i in attrs:
                if i in tt.keys():
                    t[i] = tt[i]
            return t
