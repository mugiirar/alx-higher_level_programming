#!/usr/bin/python3
"""implementation of the base class"""

from models.base import Base


class Rectangle(Base):
    """defining body of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """private width attribute
        """
        return self.__width

    @width.setter
    def width(self, n_width):
        """setting the private attribute width
        """
        if type(n_width) != int:
            raise TypeError("width must be an integer")
        if n_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = n_width
        

    @property
    def height(self):
        """private attribute height
        """
        return self.__height

    @height.setter
    def height(self, n_height):
        """setting the height
        """
        if type(n_height) != int:
            raise TypeError("height must be an integer")
        if n_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = n_height

    @property
    def x(self):
        """returning the private attribute x
        """
        return self.__x

    @x.setter
    def x(self, n_x):
        """setting the private attribute x
        """
        if type(n_x) != int:
            raise TypeError("x must be an integer")
        if n_x < 0:
            raise ValueError("x must be > 0")
        self.__x = n_x

    @property
    def y(self):
        """return the private attribute y
        """
        return self.__y

    @y.setter
    def y(self, n_y):
        """setting the private attribute y
        """
        if type(n_y) != int:
            raise TypeError("y must be an integer")
        if n_y < 0:
            raise ValueError("y must be > 0")
        self.__y = n_y

    def area(self):
        """calculating area
        """
        return (self.__width * self.__height)

    def display(self):
        """dispalying the location of the figure
        """
        z = 0
        while (z < self.__y):
            print("")
            z += 1

        k = 0
        while (k < self.__height):
            b = 0
            while (b < self.__x):
                print(" ", end='')
                b += 1
            p = 0
            while (p < self.__width):
                print("#", end='')
                p += 1
            print()
            k += 1


    def __str__(self):
        """string representation of the object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        """updating attributes of the rectangle
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        p = len(args)
        k = 0
        while (k < p):
            if k == 0:
                self.id = args[0]
            if k == 1:
                self.width = args[1]
            if k == 2:
                self.height = args[2]
            if k == 3:
                self.x = args[3]
            if k == 4:
                self.y = args[4]
            k += 1

    def to_dictionary(self):
        """making a dictionary of the object
        """
        my_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return my_dict

