#!/usr/bin/python3
"""
A function that prints a square with the character #
"""


def print_square(size):
    """
    Function that prints a square with the character #
    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
