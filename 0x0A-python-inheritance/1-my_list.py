#!/usr/bin/python3
"""
Module docs
"""


class MyList(list):
    """
    class doc
    """

    def print_sorted(self):
        """
        func doc
        """
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
