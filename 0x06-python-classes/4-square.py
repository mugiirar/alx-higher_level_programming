#!/usr/bin/python3

#!/usr/bin/python3
"""definition of class"""


class Square:
    """body """
    def __init__(self, size=0):
        """Square"""
        self.__size = size

    def size(self):
        return (self.__size)


    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return(self.__size * self.__size)
