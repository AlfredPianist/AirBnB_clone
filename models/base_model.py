#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""base_model module.
- Class BaseModel - A base class for the rest of the classes
- Instance Attributes (public):
      - id: The id of the instance.
      - created_at: The instance's creation time.
      - updated_at: The instance's update time.
- Methods (public):
      - save: Updates the instance's update time.
      - to_dict: Dictionary representation of the instance.
      - __str__: String representation of the instance.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The BaseModel class from which the rest of classes will inherit."""

    def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of a BaseModel instance.
        Returns:
            str: The string representation of a BaseModel object.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the BaseModel instance updating its updated_at attribute."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Dictionary representation of a BaseModel instance for future
        JSON serialization.
        Returns:
            dict: The dictionary representation of a BaseModel object.
        """
        base_dict = {"__class__": type(self).__name__}
        for key, value in self.__dict__.items():
            if key in ["updated_at", "created_at"]:
                value = getattr(self, key).isoformat()
            base_dict[key] = value
        return base_dict
