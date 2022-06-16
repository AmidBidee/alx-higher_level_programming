#!/usr/bin/python3
"""
square module

Class: Square(Rectangle)
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    square object class, inherits from Rectangle

    Attributes:
        id(int): id of object
        __width(int): width of object
        __height(int): height of object
        __x(int): x
        __y(int): y

    Methods:
        to_dict[inherited]: Returns dictionary represention of objects
        update[inherited]: updates object attribute value
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates a square instance with the following args;

        Args:
            size(int): size of square
            x(int): x value
            y(int): y value
            id(int): id of object

        __init__() calls the super class .__init__() this initializes the square to inherits
            the it's object
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates attribute value
        """
        iattr = {
            0: 'id',
            1: 'size',
            2: 'x',
            3: 'y',
        }
        kattr = [
            'id',
            'size',
            'x',
            'y',
        ]

        if args:
            i = 0
            for arg in args:
                if iattr[i] == 'id':
                    self.validate_args(id=arg)
                setattr(self, iattr[i], arg)
                i += 1

        if kwargs:
            for arg in kwargs:
                if arg in kattr:
                    if arg == 'id':
                        self.validate_args(id=kwargs[arg])
                    setattr(self, arg, kwargs[arg])

    def to_dictionary(self):
        """
        returns a dictionary representing the object
        """
        _dict = {}
        attr_list = ['id', 'size', 'x', 'y']

        for attr in attr_list:
            _dict[attr] = getattr(self, attr)
        return _dict

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.size,
        )
