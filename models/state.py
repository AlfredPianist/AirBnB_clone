#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""state module.
- Class State - A state class to save data of the users
- Class Attributes (public):
      - name: The state's name.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state class for storing user data, which inherits from State.
    Attributes:
        name (str): The state's name.
    """
    name = ""
