#!/usr/bin/python3
"""The first class which will be a Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return a json rep of the dico """
        if list_dictionaries is None:
            return ""

        list_Json = json.dumps(list_dictionaries)
        return list_Json

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None:
            return ""

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_objs to a file """
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)
        file_name = cls.__name__ + ".json"
        with open(file_name, mode='w', encoding='utf-8') as a_file:
            json.dump(content, a_file)
