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

    def to_json(self, attrs=None):
        """ Method that returns directory description """

        if isinstance(attrs, list) and all(isinstance(a, str)
                                           for a in attrs):
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for a in json:
            self.__dict__[a] = json[a]
