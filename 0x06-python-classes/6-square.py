#!/usr/bin/python3
"""class defination"""


class Square:
    """body of the class"""

    def __init__(self, size=0, position=(0, 0)):
        """the constructor"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of a square."""
        return (self.__size * self.__size)

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if (len(value) != 2 or type(value) is not tuple or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """square with the character"""
        p = 0
        while p < self.__position[1]:
            print("")
            p += 1

        k = 0
        while k < self.__size:
            m = 0
            while m < self.__position[0]:
                print(" ", end="")
                m += 1
            n = 0
            while n < self.__size:
                print("#", end="")
                n += 1
            print("")
            k += 1
