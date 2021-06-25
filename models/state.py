#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""state module.
- Class State - A state class to save data of the users
- Instance Attributes (public):
      - name: string - empty string
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
class State(BaseModel):
      """A state class for storing user data, which inherits from State."""
      def __init__(self, *args, **kwargs):
        """The class constructor.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
      super().__init__(id)
      self.name = str("")
