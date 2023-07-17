#!/usr/bin/python3
"""
FileStorage - Serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
import os.path    # Checking if a file exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON files to instances
    """

    # Private Class Attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file path
        """

        serialized = {key: obj.to_dict() for (key, obj) in self.__objects.items()}

        with open(self.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r") as f:
                    myFile = json.load(f)

                    for key, value in myFile.items():
                        classname, obj_id = key.split('.')
                        self.__objects[key] = eval(classname)(**value)
        except:
            pass
