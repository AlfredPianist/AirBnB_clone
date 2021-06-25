#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""review module.
- Class Review - A review class to save data of the users
- Instance Attributes (public):
      - place_id: string - empty string: it will be the Place.id
      - user_id: string - empty string: it will be the User.id
      - text: string - empty string
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
class Review(BaseModel):
      """A city class for storing user data, which inherits from BaseModel."""
      def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
      super().__init__(id)
      self.place_id = str("")
      self.user_id = str("")
      self.text = str("")