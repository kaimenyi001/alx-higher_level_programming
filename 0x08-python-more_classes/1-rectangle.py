#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    Instantiation with optional width and heigh
    """

    def __init__(self, width=0, height=0):
        """ Initialization method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property width getter """
        return self.__width

    @property
    def height(self):
        """ property height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """ property width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ property height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
