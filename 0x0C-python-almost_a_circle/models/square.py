#!/usr/bin/python3
"""
module doc
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class for square object
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        square initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        handles string what happens when the string
        function is called on the instance
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kargs):
        """
        updates the instance
        """
        argl = ['id', 'size', 'x', 'y']
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
                if j in argl:
                    setattr(self, j, l)

    def to_dictionary(self):
        """
        it retrurns the dictionary representation of a square
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    @property
    def size(self):
        """
        getter
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        size setter
        """
        self.width = val
        self.height = val
