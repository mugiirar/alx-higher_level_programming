#!/usr/bin/python3
"""class defination"""


class Square:
    """body of the class"""

    def __init__(self, size):
        """the constructor"""
        self.size = size

    @property
    def size(self):
        """getter for __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of a square."""
        return (self.__size * self.__size)

    def my_print(self):
        """square with the character"""
        p = 0
        while p < self.__size:
            k = 0
            while k < self.__size:
                print("#", end="")
                k += 1
            p += 1
            print("")
        if self.__size == 0:
            print("")
