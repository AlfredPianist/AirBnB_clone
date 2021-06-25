#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""city module.
- Class City - A city class to save data of the users
- Instance Attributes (public):
      - state_id: string - empty string: it will be the State.id
      - name: string - empty string
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
class City(BaseModel):
      """A city class for storing user data, which inherits from BaseModel."""
      def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
      super().__init__(id)
      self.state_id = str("")
      self.name = str("")