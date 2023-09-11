#!/usr/bin/python3
"""class for geometry"""


class BaseGeometry:
    """defination of this class"""
    def area(self):
        """complain"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validating inputs"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
