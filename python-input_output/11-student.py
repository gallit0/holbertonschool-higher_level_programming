#!/usr/bin/python3
"""Module"""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        d = {}
        for i in attrs:
            if i in self.__dict__:
                d[i] = self.__dict__[i]
        return d

    def reload_from_json(self, json):
        pass
