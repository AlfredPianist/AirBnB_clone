#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""amenity module.
- Class Amenity - A amenity class to save data of the users
- Class Attributes (public):
      - name: The amenity's name.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A amenity class for storing user data, which inherits from BaseModel.
    Attributes:
        name (str): The amenity's name.
    """
    name = ""
