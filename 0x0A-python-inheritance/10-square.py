#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from Rectangle class """
    def __init__(self, size):
        """ Initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Returns a string with the area """
        return super().area()
