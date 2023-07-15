#!/usr/bin/python3
"""
FileStorage - Serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
import os.path    # Checking if a file exists


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        """
        FileStorage.__objects["{}.{}".format(__class__.__name__, self.id)] = obj    # Test this

    def save(self):
        """
        Serializes __objects to the JSON file path
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file
        """
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r") as f:
                    myFile = f.read()
                    FileStorage.__objects = json.loads(myFile)
        except:
            pass
