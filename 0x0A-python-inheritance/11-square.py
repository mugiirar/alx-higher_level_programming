#!/usr/bin/python3
"""rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """body of the class"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
