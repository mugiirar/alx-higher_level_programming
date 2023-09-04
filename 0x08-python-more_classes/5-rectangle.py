#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """rectangle defination"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        if self.__width != 0 and self.__height != 0:
            return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        if self.__width != 0 and self.__height != 0:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''

        string = ''
        k = 0
        while k < self.__height:
            l = 0
            while l < self.__width:
                string += '#'
                l += 1
            string += '\n'
            k += 1
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        print("Bye rectangle...")
