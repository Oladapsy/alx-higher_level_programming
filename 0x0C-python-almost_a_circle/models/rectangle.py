#!/usr/bin/python3
""" the class Rectangle that inherits from Base"""
from models.base import Base
""" this is importing the base object defined in model dir in file base.py"""


class Rectangle(Base):
    """ THe class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ the with getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ the width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """ the setter for x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ The area of a Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        for length in range(self.__height):
            print("#" * self.__width, end='')
            print()

        def __str__(self):
            """ it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
            class_id = self.id
            x = self.x
            y = self.y
            width = self.width
            height = height.width
            return (f"[Rectangle] ({class_id}) {x}/{y} - {width}/{self.height}")
