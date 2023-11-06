#!/usr/bin/python3
"""MyList class Module"""


class MyList(list):
    """Customized list class"""
    def print_sorted(self):
        """Public instance method that prints the list in sorted
        (ascending sort) order
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
