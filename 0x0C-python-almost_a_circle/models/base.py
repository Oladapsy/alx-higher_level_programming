#!/usr/bin/python3
"""The first class which will be a Base class """


class Base:
    """ A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization or instantation of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
