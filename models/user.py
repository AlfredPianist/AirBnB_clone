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

    def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(**kwargs)
