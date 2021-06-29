#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""city module.
- Class City - A city class to save data of the users
- Class Attributes (public):
      - state_id: The state's id.
      - name: The city's name.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A city class for storing user data, which inherits from BaseModel.
    Attributes:
        state_id (str): The state's id.
        name (str): The city's name.
    """
    state_id = ""
    name = ""
