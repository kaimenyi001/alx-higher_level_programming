#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """ Class that inherits from class int"""

    def __eq__(self, other):
        """ Returns != """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Returns == """
        return int.__eq__(self, other)
