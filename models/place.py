#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""place module.
- Class Place - A place class to save data of the users
- Class Attributes (public):
      - city_id: The city's id.
      - user_id: The user's id.
      - name: The place's name.
      - description: The place's description.
      - number_rooms: The place's number of rooms.
      - number_bathrooms: The place's number of bathrooms.
      - max_guest: The place's maximum number of guests.
      - price_by_night: The place's price by night.
      - latitude: The place's latitude.
      - longitude: The place's longitude.
      - amenity_ids: The list of amenity ids.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place class for storing user data, which inherits from BaseModel.
    Attributes:
        city_id (str): The city's id.
        user_id (str): The user's id.
        name (str): The place's name.
        description (str): The place's description.
        number_rooms (int): The place's number of rooms.
        number_bathrooms (int): The place's number of bathrooms.
        max_guest (int): The place's maximum number of guests.
        price_by_night (int): The place's price by night.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids (list of str): The list of amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
