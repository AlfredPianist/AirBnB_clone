#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""amenity module.
- Class Amenity - A amenity class to save data of the users
- Instance Attributes (public):
      - name: string - empty string
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A amenity class for storing user data, which inherits from BaseModel.
    """
    def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.name = ""
        super().__init__(**kwargs)
