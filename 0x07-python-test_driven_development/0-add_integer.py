#!/usr/bin/python3
"""It's an integer addition function."""


def add_integer(a, b=98):
    """
    Return an integer: the addition of a and b.
    a and b must be first casted to integers if they are float
    Raises TypeError: If either of a or b is a non-integer and non-float.
    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return ( a + b )
