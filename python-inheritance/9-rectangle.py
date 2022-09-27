#!/usr/bin/python3
"""Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Module"""


class Rectangle(BaseGeometry):
    """Rectangle inherts from Base geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return (f'[Rectangle] {self.__width}/{self.__height}')
