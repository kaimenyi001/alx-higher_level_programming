#!/usr/bin/python3
class MyList(list):
    """
    Class that inherits the attributes references of class list
    """
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
