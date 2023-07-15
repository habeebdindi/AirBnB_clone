#!/usr/bin/python3
import uuid
from datetime import datetime
"""
"""


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        """
        updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        """
        dict_kv = {}
        dict_kv['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at":
                dict_kv[key] = self.created_at.isoformat("T", "microseconds")
            elif key == "updated_at":
                dict_kv[key] = self.updated_at.isoformat("T", "microseconds")
            else:
                dict_kv[key] = value
        return dict_kv
