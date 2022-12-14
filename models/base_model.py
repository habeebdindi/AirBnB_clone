#!/usr/bin/python3
"""
This module contains a Super Class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This is a Base class, it means other classes can inherit its \
    attributes and methods.

    Attributes:
        id (str): A unique identifier for each created instance.
        created_at (datetime): Time instance was created.
        updated_at (datetime): Time instance was updated.
    """

    def __init__(self, *args, **kwargs):
        """
        initializing(creating) an instance using a dict representation

        Args:
        args: variable arguments, unmapped
        kwargs: variable mapped arguments
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                form = '%Y-%m-%dT%H:%M:%S.%f'
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, form)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

        models.storage.new(self)

    def __str__(self):
        """
        make a string representation of the class.

        """
        string = ""
        string += "[{}] ".format(type(self).__name__) + \
                  "({}) ".format(self.id) + "{}".format(self.__dict__)
        return string

    def save(self):
        """
        Update the time whenever a change is made to object.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dict representation of the instance.
        """
        m_dict = self.__dict__.copy()
        m_dict["__class__"] = type(self).__name__
        m_dict["created_at"] = self.created_at.isoformat()
        m_dict["updated_at"] = self.updated_at.isoformat()
        return m_dict
