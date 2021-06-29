#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""city module.
- Class City - A city class to save data of the users
- Class Attributes (public):
      - city_id: The city's id.
      - name: The city's name.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city class for storing user data, which inherits from BaseModel.
    Attributes:
        city_id (str): The city id.
        name (str): The city's name.
    """
    city_id = ""
    name = ""
