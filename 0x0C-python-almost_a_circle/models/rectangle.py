#!/usr/bin/python3
"""
module doc
"""

from models.base import Base


class Rectangle(Base):
    """
    rectangle class that inherites the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        handles string what happens when the string
        function is called on the instance
        """
        return "[Rectangele] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def area(self):
        """
        returns the area of the instance
        """
        return self.__height * self.__width

    def display(self):
        """
        print a the triangle structure
        """
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print("{}{}".format(' ' * self.__x, '#' * self.__width))

    def update(self, *args, **kargs):
        """
        updates the instance
        """
        argl = ['id', 'width', 'height', 'x', 'y']
        argn = 0
        if len(args) != 0:
            for i in args:
                if argn == 0:
                    self.id = i
                else:
                    setattr(self, argl[argn], i)
                argn += 1
        else:
            for j, l in kargs.items():
                setattr(self, j, l)

    def to_dictionary(self):
        """
        it retrurns the dictionary representation of a rectangle
        """
        return {
                'x': self.x,
                'width': self.width,
                'id': self.id,
                'height': self.height,
                'y': self.y
                }

    @property
    def width(self):
        """
        getter
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        setter
        """
        if type(val) != int:
            raise TypeError('width must be an integer')
        if val < 1:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        setter
        """
        if type(val) != int:
            raise TypeError('height must be an integer')
        if val < 1:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """
        getter
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        setter
        """
        if type(val) != int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """
        getter
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        setter
        """
        if type(val) != int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val
