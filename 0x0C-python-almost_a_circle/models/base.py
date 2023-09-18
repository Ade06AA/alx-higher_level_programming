#!/usr/bin/python3
"""
module doc
"""
import json


class Base:
    """
    this is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert the dictionary representation to json
        """
        if type(list_dictionaries) is list:
            if len(list_dictionaries) == 0:
                return json.dumps([])
            else:
                return json.dumps(list_dictionaries)
        elif list_dictionaries is None:
            return json.dumps([])

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the json string reprwesentation
        """
        new = []
        if json_string is None or json_string == "":
            return new
        new = json.loads(json_string)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """
        it writes the json string representation of list_obj to a file
        <Class name>.json
        """
        newl = []
        for i in list_objs:
            newl.append(i.to_dictionary())
        temp = Base.to_json_string(newl)
        with open("{}.json".format(cls.__name__),
                  'w', encoding='utf-8') as nfile:
            nfile.write(temp)

    @classmethod
    def create(cls, **dictionary):
        """
        it returns an instance with all attributes alredy set
        """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)
        else:
            new = cls()
            return new
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        it returns an instance with all attributes alredy set
        """
        with open("{}.json".format(cls.__name__),
                  'r', encoding='utf-8') as jfile:
            content = Base.from_json_string(jfile.read())
        NewObjectList = []
        for i in content:
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            elif cls.__name__ == 'Square':
                new = cls(1)
            else:
                new = cls()
                return new
            new = cls(1, 1)
            new.update(**i)
            NewObjectList.append(new)
        return NewObjectList
