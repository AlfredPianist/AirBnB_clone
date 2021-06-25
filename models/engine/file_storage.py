#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""file_storage module.
- Class FileStorage - A class containing all the storage methods.
- Class Attributes (private):
      - __file_path: The path of the .json file.
      - __objects: A dictionary containing all objects instantiated.
- Methods (public):
      - all: Returns the dictionary __objects.
      - new: Inserts a new object to the __objects dictionary.
      - save: Saves the contents of the __objects dictionary to a json file.
      - reload: Loads the contents of the json file and instantiates
                the loaded objects.
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """The FileStorage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects.
        Returns:
            dict: The dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Inserts a new object to the __objects dictionary.
        Args:
            obj (obj): The object to be inserted to the __objects dictionary.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves the contents of the __objects dictionary to a json file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            if FileStorage.__objects is not None:
                json_dict = {obj_key: obj_val.to_dict()
                             for obj_key, obj_val
                             in FileStorage.__objects.items()}
                json.dump(json_dict, f)

    def reload(self):
        """Loads the contents of the json file and instantiates the loaded
        objects.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
            for key, val in json_dict.items():
                val = eval(val["__class__"])(**val)
                FileStorage.__objects[key] = val
        except IOError:
            pass
