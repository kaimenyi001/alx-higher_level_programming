#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry:
    """ Class that defines the attributes of geometric Shapes """

    def area(self):
        """ Method that defines the area of a geometric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that recieves the value property
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
