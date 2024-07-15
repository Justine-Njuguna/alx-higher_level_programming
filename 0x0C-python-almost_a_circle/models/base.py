#!/usr/bin/python3

"""
    Defines a base model class.
"""


import json
import csv


class Base:
    """
    Represents the base model
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON str representation of list_dict
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by json_string
        """
        if json_string is None or json_string.strip() == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            # Create a dummy Rectangle instance
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            # Create a dummy Square instance
            dummy_instance = Square(1)
        else:
            raise ValueError("Unsupported class type")

        # Update attributes using **kwargs from dictionary
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**data) for data in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs into a CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Unsupported class type")
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        from models.rectangle import Rectangle
        from models.square import Square
        """
        Deserializes list_objs from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y = map(int, row)
                        obj = Rectangle(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        obj = Square(size, x, y, id)
                    else:
                        raise ValueError("Unsupported class type")
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []
