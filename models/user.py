#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""user module.
- Class User - The User class, inherited from BaseModel
- Instance Attributes (public):
      - email: The user's email.
      - password: The user's password.
      - first_name: The user's first name.
      - last_name: The user's last name.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User class inherited from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
