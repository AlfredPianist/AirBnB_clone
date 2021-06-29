#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""review module.
- Class Review - A review class to save data of the users
- Class Attributes (public):
      - place_id: The place's id.
      - user_id: The user's id.
      - text: The user's review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A city class for storing user data, which inherits from BaseModel.
    Attributes:
        place_id (str): The place's id.
        user_id (str): The user's id.
        text (str): The user's review.
    """
    place_id = ""
    user_id = ""
    text = ""
