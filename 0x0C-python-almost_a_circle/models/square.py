#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
                self.x = args[2]
            if k == 3:
                self.y = args[3]
            k += 1

    def to_dictionary(self):
        my_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return my_dict

