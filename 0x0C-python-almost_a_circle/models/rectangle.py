#!/usr/bin/python3

'''Rectangle module

class: Rectangle
    __init__(widget, height, x=0, y=0)

methods:

    Rectangle.validate_args(self, **kwargs)

    Rectangle.width(self, value)

    Rectangle.height(self, value)
'''
from models.base import Base


class Rectangle(Base):
    """
    Rectangle object class, inherits from the from base.Base class
    creates a Rectangle object instance with a width and height

    attributes:
        private -->
        __width: width
        __height: height
        __x: x
        __y: y

    Methods:
        validate_args(self, *kwargs):
                validates the arguments passed in, returns true if
                all requirements are passed and raises an exception if not
    """
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor

        Rectangle.__init__(self, width, height x=0, y=0)
            instatiate a Rectangle object with a width and height
        Initializes a new rectangle object.
        Args:
            width (int): The width of this rectangle.
            height (int): The height of this rectangle.
            x (int): The horizontal position of this rectangle.
            y (int): The vertical position of this rectangle.
            id (int): The id of this rectangle.
        """

        self.validate_args(width=width, height=height, x=x, y=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id=id)

    @property
    def width(self):
        """
        Retrieves the value of the private instance attribute [__width]
        and returns it
        attr: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        assigns value to the private instance attribute [__width]
        if value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(width=value)
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the private instance attribute [__height]
        and returns it
        attr: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        assigns the value to the private instance attribute [__height]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(height=value)
        self.__height = value

    @property
    def x(self):
        """
        Retrieves the value of the private instance attribute [__x]
        and returns it
        attr: self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        assigns the value to the private instance attribute [__x]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(x=value)
        self.__x = value

    @property
    def y(self):
        """
        Retrieves the value of the private instance attribute [__y]
        and returns it
        attr: self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        ssigns the value to the private instance attribute [__y]
        if the value is validated and self.validate_args(**kwargs) returns True
        """
        self.validate_args(y=value)
        self.__y = value

    def __width__(self, value):
        self.width = value

    def __height__(self, value):
        self.height = value

    def __x__(self, value):
        self.x = value

    def __y__(self, value):
        self.y = value

    def validate_args(self, **kwargs):
        """
        public instance method -->
        validate_args(self, *kwargs):
                validates the arguments passed in, returns true if
                all requirements are passed and raises an exception if not
        """
        for arg in kwargs:
            if type(kwargs[arg]) != int:
                raise TypeError('{} must be an integer'.format(arg))

            if arg in ('width', 'height') and kwargs[arg] <= 0:
                raise ValueError('{} must be > 0'.format(arg))

            if arg in ('x', 'y') and kwargs[arg] < 0:
                raise ValueError('{} must be >= 0'.format(arg))
        return True

    def area(self):
        """
        public instance method -->
            area(self):
                should return the area value of the rectangle object
        """
        value = self.__width * self.__height
        return value

    def display(self):
        """
        displays the rectangle object with the width and height
        using hashes(#), does not take x,y into consideration
        """
        width = self.__width
        height = self.__height

        for h in range(height):
            for w in range(width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """
        updates attribute value
        """
        iattr = {
            0: 'id',
            1: 'width',
            2: 'height',
            3: 'x',
            4: 'y',
        }
        kattr = [
            'id',
            'width',
            'height',
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
        attr_list = ['id', 'width', 'height', 'x', 'y']

        for attr in attr_list:
            _dict[attr] = getattr(self, attr)
        return _dict

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )
