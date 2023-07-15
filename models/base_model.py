#!/usr/bin/python3
import uuid
from datetime import datetime
# from . import storage


"""
"""


class BaseModel:
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        from . import storage
        if kwargs:
            for key, value in kwargs.items():
                if key in  ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        storage.save()

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
