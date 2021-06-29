#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""user module.
- Class User - The User class, inherited from BaseModel
- Class Attributes (public):
      - email: The user's email.
      - password: The user's password.
      - first_name: The user's first name.
      - last_name: The user's last name.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class inherited from BaseModel.
    Attributes:
        email (str): The user's email.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
