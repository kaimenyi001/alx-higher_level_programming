#!/usr/bin/python3
"""
Module that defines a Student
"""


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """ Intialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
