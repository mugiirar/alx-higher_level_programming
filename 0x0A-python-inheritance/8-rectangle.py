#!/usr/bin/python3


"""geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle definition"""


    def __init__(self, width, height):
        super().integer_validator("width", width)

        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
